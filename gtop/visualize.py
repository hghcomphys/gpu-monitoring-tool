from gtop.metrics import Metrics
from typing import Any

PlotHandle = Any


def visualize(
    plt: PlotHandle,
    metrics: Metrics,
) -> None:
    plt.clt()
    plt.cld()
    plt.subplots(1, 2)
    plt.theme("matrix")
    plt.plotsize(100, 20)

    # --------------
    plt.subplot(1, 2)
    plt.plot(metrics.times, metrics.tx_values, label="TX", marker="dot")
    plt.plot(metrics.times, metrics.rx_values, label="RX", marker="dot")

    plt.title("GPU PCIe Throughput")
    plt.xlabel("Time (s)")
    plt.ylabel("Throughput (MB/s)")
    plt.ylim(0, max(1, max(metrics.tx_values + metrics.rx_values) * 1.2))

    # --------------
    plt.subplot(1, 1)
    plt.plot(metrics.times, metrics.util_values, label="Process", marker="dot")
    plt.plot(metrics.times, metrics.mem_values, label="Memory", marker="dot")

    plt.title("GPU Utilization")
    plt.xlabel("Time (s)")
    plt.ylabel("Utilization (%)")
    plt.ylim(0, 100)
    plt.show()
