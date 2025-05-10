from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol, Sequence,Optional
import pynvml

from gtop.device import DeviceHandle
from typing import Any, Tuple


class MetricInterface(Protocol):
    def measure() -> Any: ...


@dataclass
class GpuComputeRunningProcesses(MetricInterface):
    handle: DeviceHandle

    def measure(self) -> Sequence:
        return pynvml.nvmlDeviceGetComputeRunningProcesses(self.handle)


@dataclass
class GpuInfoMetric(MetricInterface):
    handle: DeviceHandle

    def measure(self) -> str:
        return pynvml.nvmlDeviceGetName(self.handle)


@dataclass
class GpuTemperatureMetric(MetricInterface):
    handle: DeviceHandle

    def measure(self) -> float:
        return pynvml.nvmlDeviceGetTemperature(self.handle, pynvml.NVML_TEMPERATURE_GPU)


@dataclass
class GpuPowerUsageMetric(MetricInterface):
    handle: DeviceHandle

    def measure(self) -> Optional[float]:
        try:
            power_mw = pynvml.nvmlDeviceGetPowerUsage(self.handle)
            return power_mw * 0.001  # watts
        except pynvml.NVMLError:
            return None 

@dataclass
class PciThroughputMetric(MetricInterface):
    handle: DeviceHandle

    def measure(self) -> Tuple[float, float]:
        tx = (
            pynvml.nvmlDeviceGetPcieThroughput(
                self.handle,
                pynvml.NVML_PCIE_UTIL_TX_BYTES,
            )
            / 1024
        )
        rx = (
            pynvml.nvmlDeviceGetPcieThroughput(
                self.handle,
                pynvml.NVML_PCIE_UTIL_RX_BYTES,
            )
            / 1024
        )
        return tx, rx  # MB


@dataclass
class GpuUtilizationMetric(MetricInterface):
    handle: DeviceHandle

    def measure(self) -> float:
        util = pynvml.nvmlDeviceGetUtilizationRates(self.handle)
        return util.gpu


@dataclass
class GpuMemoryMetric(MetricInterface):
    handle: DeviceHandle

    def measure(self) -> Tuple[float, float]:
        mem_info = pynvml.nvmlDeviceGetMemoryInfo(self.handle)
        mem_used = int(mem_info.used / 1024**2)
        mem_total = int(mem_info.total / 1024**2)
        return mem_used, mem_total  # MB


@dataclass
class GpuMetrics:
    pci_throughput: PciThroughputMetric
    utilization: GpuProcessMetric
    memory: GpuMemoryMetric
    info: GpuInfoMetric
    processes: GpuComputeRunningProcesses
    power_usage: GpuPowerUsageMetric
    temperature: GpuTemperatureMetric

    @classmethod
    def for_device(cls, handle: DeviceHandle):
        return cls(
            PciThroughputMetric(handle),
            GpuUtilizationMetric(handle),
            GpuMemoryMetric(handle),
            GpuInfoMetric(handle),
            GpuComputeRunningProcesses(handle),
            GpuPowerUsageMetric(handle),
            GpuTemperatureMetric(handle),
        )
