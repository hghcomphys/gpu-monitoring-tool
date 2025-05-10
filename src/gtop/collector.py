import time
import psutil
from dataclasses import dataclass, field
from typing import List
from gtop.config import Config
from gtop.metrics import GpuMetrics


@dataclass
class CollectedGpuMetrics:
    timestamp: float
    pci_tx: float
    pci_rx: float
    utilization: float
    memory: float
    name: str
    processes: str
    memory_total: float
    temperature: float
    power_usage: float

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"Time={self.timestamp:0.2f}(s)"
            f", Utilization={self.utilization:0.2f}(%)"
            f", Memory={self.memory:0.2f}(%)"
            f", PCI-TX={self.pci_tx:0.2f}(MB/s)"
            f", PCI-RX={self.pci_rx:0.2f}(MB/s)"
            # f", Power={self.power_usage:0.2f}(W)"
            ")"
        )


@dataclass
class CollectedGpuMetricsBuffer:
    size: int
    buffer: List[CollectedGpuMetrics] = field(default_factory=list)

    def append(self, item: CollectedGpuMetrics) -> None:
        self.buffer.append(item)
        if len(self.buffer) > self.size:
            self.buffer = self.buffer[-self.size :]

    def __iter__(self):
        for item in self.buffer:
            yield item

    @property
    def last(self) -> CollectedGpuMetrics:
        return self.buffer[-1]

    @property
    def first(self) -> CollectedGpuMetrics:
        return self.buffer[0]


def collect(
    metrics: GpuMetrics,
    start_time: float,
    cfg: Config,
) -> CollectedGpuMetrics:
    now = time.time() - start_time
    tx, rx = metrics.pci_throughput.measure()
    utilization = metrics.utilization.measure()
    mem_used, mem_total = metrics.memory.measure()
    gpu_name = metrics.info.measure()
    temperature = metrics.temperature.measure()
    power_usage = metrics.power_usage.measure()
    processes = metrics.processes.measure()
    processes_text = ""
    for index, p in enumerate(processes, start=1):
        pid = p.pid
        ps = psutil.Process(pid)
        if index == 1:
            processes_text = "Index | PID | Username | Command\n"
        processes_text += f"[{index}] {pid}, {ps.username()}, {' '.join(ps.cmdline())}\n"

    return CollectedGpuMetrics(
        timestamp=max(now, cfg.collector_min_time_interval),
        pci_tx=tx,
        pci_rx=rx,
        utilization=utilization,
        memory=mem_used / mem_total * 100,
        name=gpu_name,
        processes=processes_text,
        memory_total=mem_total,
        temperature=temperature,
        power_usage=power_usage,
    )

