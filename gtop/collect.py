import time
import pynvml
from gtop.device import DeviceHandle
from gtop.metrics import Metrics


def collect(
    handle: DeviceHandle,
    metrics: Metrics,
    start_time: float,
    max_points: int,
):
    now = time.time() - start_time
    tx = pynvml.nvmlDeviceGetPcieThroughput(handle, pynvml.NVML_PCIE_UTIL_TX_BYTES) / (
        1024
    )  # MB
    rx = pynvml.nvmlDeviceGetPcieThroughput(handle, pynvml.NVML_PCIE_UTIL_RX_BYTES) / (
        1024
    )  # MB
    util = pynvml.nvmlDeviceGetUtilizationRates(handle)
    mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    mem_used = int(mem_info.used / 1024**2)  # MB
    mem_total = int(mem_info.total / 1024**2)  # MB
    # -----
    metrics.times.append(round(now, 1))
    metrics.tx_values.append(tx)
    metrics.rx_values.append(rx)
    metrics.util_values.append(util.gpu)
    metrics.mem_values.append(mem_used / mem_total * 100.0)
    if len(metrics.times) > max_points:
        metrics.times = metrics.times[-max_points:]
        metrics.tx_values = metrics.tx_values[-max_points:]
        metrics.rx_values = metrics.rx_values[-max_points:]
        metrics.util_values = metrics.util_values[-max_points:]
        metrics.mem_values = metrics.mem_values[-max_points:]

