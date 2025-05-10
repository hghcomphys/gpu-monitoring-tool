from psutil import POWER_TIME_UNKNOWN
from gtop.config import Config
from gtop.collector import CollectedGpuMetricsBuffer
from typing import Any

PlotHandle = Any


def visualize(
    inputs: CollectedGpuMetricsBuffer,
    plt: PlotHandle,
    cfg: Config,
) -> None:
    if cfg.text_mode:
        printout_metrics(inputs)
        return
    plt.clt()
    plt.cld()
    plt.plotsize(cfg.visualizer_plot_size)
    plt.theme(cfg.visualizer_plot_theme)
    plt.subplots(2, 2)
    # --------------------
    plt.subplot(1, 1)
    gpu_info = (
        (
            f"{inputs.last.name}"
            f"\nTotal Memory: {inputs.last.memory_total:0.0f} (MB)"
            f"\nTemperature: {inputs.last.temperature:0.1f} (°C)"
        )
        + (f"\nPower Usage: {inputs.last.power_usage:0.1f} (W)"
        if inputs.last.power_usage is not None
        else "")
    )
    plt.text(gpu_info, 0, 1)
    plt.xticks([])
    plt.yticks([])
    # plt.xaxes(False, True)
    plt.yaxes(False, False)
    plt.ylim(0, 1)
    plt.title("GPU Information")
    # --------------------
    plt.subplot(2, 1)
    processes = (
        inputs.last.processes
        if inputs.last.processes
        else "No Compute Running Processes"
    )
    plt.text(processes, 0, 1)
    plt.xticks([])
    plt.yticks([])
    # plt.xaxes(False, True)
    plt.yaxes(False, False)
    plt.ylim(0, 1)
    plt.title("GPU Processes")
    # --------------------
    plt.subplot(1, 2)
    names = [
        "Memory",
        "Utilization",
    ]
    values = [
        inputs.last.memory,
        inputs.last.utilization,
    ]
    plt.bar(
        names,
        values,
        orientation="h",
        width=2 / 5,
    )
    plt.title("GPU Utilization (%)")
    plt.xlim(0, 100)
    # --------------------
    plt.subplot(2, 2)
    names = [
        "PCI-TX",
        "PCI-RX",
    ]
    values = [
        inputs.last.pci_rx,
        inputs.last.pci_tx,
    ]
    plt.bar(
        names,
        values,
        orientation="h",
        width=2 / 5,
    )
    plt.title("GPU PCIe Throughput (MB/s)")
    plt.xlim(0, max(1, max(inputs.last.pci_tx, inputs.last.pci_rx) * 1.2))
    # --------------------
    plt.sleep(cfg.update_interval)
    plt.show()


def printout_metrics(inputs: CollectedGpuMetricsBuffer) -> None:
    print(inputs.last)
