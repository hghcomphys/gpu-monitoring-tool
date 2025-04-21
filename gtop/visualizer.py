from gtop.config import Config
from gtop.metrics import Metrics
from typing import Any

PlotHandle = Any


def visualize(
    metrics: Metrics,
    plt: PlotHandle,
    cfg: Config,
) -> None:
    plt.clt()
    plt.cld()
    plt.subplots(1, 2)
    plt.theme(cfg.visualizer_plot_theme)
    plt.plotsize(cfg.visualizer_plot_size)
    # --------------
    plt.subplot(1, 2)
    plt.plot(
        metrics.times,
        metrics.tx_values,
        label="TX",
        marker=cfg.visualizer_plot_marker,
    )
    plt.plot(
        metrics.times,
        metrics.rx_values,
        label="RX",
        marker=cfg.visualizer_plot_marker,
    )

    plt.title("GPU PCIe Throughput")
    plt.xlabel("Time (s)")
    plt.ylabel("Throughput (MB/s)")
    plt.ylim(0, max(1, max(metrics.tx_values + metrics.rx_values) * 1.2))

    # --------------
    plt.subplot(1, 1)
    plt.plot(
        metrics.times,
        metrics.util_values,
        label="Process",
        marker=cfg.visualizer_plot_marker,
    )
    plt.plot(
        metrics.times,
        metrics.mem_values,
        label="Memory",
        marker=cfg.visualizer_plot_marker,
    )

    plt.title("GPU Utilization")
    plt.xlabel("Time (s)")
    plt.ylabel("Utilization (%)")
    plt.ylim(0, 100)
    plt.sleep(cfg.update_interval)
    plt.show()
