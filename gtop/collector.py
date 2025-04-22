import time
from dataclasses import dataclass, field
from typing import List
from gtop.config import Config
from gtop.device import DeviceHandle
from gtop.metrics import Metrics


@dataclass
class CollectedMetrics:
    timestamp: float
    pci_tx: float
    pci_rx: float
    process: float
    memory: float


@dataclass
class CollectedMetricsBuffer:
    size: int
    buffer: List[CollectedMetrics] = field(default_factory=list)

    def append(self, item: CollectedMetrics) -> None:
        self.buffer.append(item)
        if len(self.buffer) > self.size:
            self.buffer = self.buffer[-self.size :]

    def __iter__(self):
        for item in self.buffer:
            yield item

    @property
    def last(self) -> CollectedMetrics:
        return self.buffer[-1]


def collect(
    metrics: Metrics,
    handle: DeviceHandle,
    start_time: float,
    cfg: Config,
) -> CollectedMetrics:
    now = time.time() - start_time
    tx, rx = metrics.pci_throughput.measure()
    process = metrics.gpu_processs.measure()
    mem_used, mem_total = metrics.gpu_memory.measure()
    return CollectedMetrics(
        timestamp=max(now, cfg.collector_min_interval),
        pci_tx=tx,
        pci_rx=rx,
        process=process,
        memory=mem_used / mem_total * 100,
    )
