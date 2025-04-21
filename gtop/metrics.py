from dataclasses import dataclass, field


@dataclass
class Metrics:
    times: list[float] = field(default_factory=list)
    tx_values: list[float] = field(default_factory=list)
    rx_values: list[float] = field(default_factory=list)
    util_values: list[float] = field(default_factory=list)
    mem_values: list[float] = field(default_factory=list)
