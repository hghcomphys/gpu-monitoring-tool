import pynvml
import plotext as plt
import time

# Initialize NVML
pynvml.nvmlInit()
handle = pynvml.nvmlDeviceGetHandleByIndex(0)

# Time and data storage
times = []
tx_values = []
rx_values = []
util_values = []
mem_values = []


# How long to sample (in seconds)
interval = 1
max_points = 30

start_time = time.time()
try:
    while True:

        now = time.time() - start_time
        tx = pynvml.nvmlDeviceGetPcieThroughput(
            handle, pynvml.NVML_PCIE_UTIL_TX_BYTES
        ) / (
            1024
        )  # MB
        rx = pynvml.nvmlDeviceGetPcieThroughput(
            handle, pynvml.NVML_PCIE_UTIL_RX_BYTES
        ) / (
            1024
        )  # MB

        util = pynvml.nvmlDeviceGetUtilizationRates(handle)
        mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        mem_used = int(mem_info.used / 1024**2)  # MB
        mem_total = int(mem_info.total / 1024**2)  # MB

        times.append(round(now, 1))
        tx_values.append(tx)
        rx_values.append(rx)
        util_values.append(util.gpu)
        mem_values.append(mem_used / mem_total * 100.0)

        if len(times) > max_points:
            times = times[-max_points:]
            tx_values = tx_values[-max_points:]
            rx_values = rx_values[-max_points:]
            util_values = util_values[-max_points:]
            mem_values = mem_values[-max_points:]

        # Clear and redraw the plot
        plt.subplots(1, 2)
        plt.clt()
        plt.cld()
        plt.theme("matrix")
        plt.plotsize(100, 20)

        # --------------
        plt.subplot(1, 2)
        plt.plot(times, tx_values, label="TX", marker="dot")
        plt.plot(times, rx_values, label="RX", marker="dot")

        plt.title("GPU PCIe Throughput")
        plt.xlabel("Time (s)")
        plt.ylabel("Throughput (MB/s)")
        plt.ylim(0, max(1, max(tx_values + rx_values) * 1.2))

        # --------------
        plt.subplot(1, 1)
        plt.plot(times, util_values, label="Process", marker="dot")
        plt.plot(times, mem_values, label="Memory", marker="dot")

        plt.title("GPU Utilization")
        plt.xlabel("Time (s)")
        plt.ylabel("Utilization (%)")
        plt.ylim(0, 100)

        plt.sleep(interval)
        plt.show()

except KeyboardInterrupt:
    # print("\n⛔ Interrupted by user.")
    pass

finally:
    # Clean up NVML
    pynvml.nvmlShutdown()
