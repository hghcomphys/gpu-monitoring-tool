from __future__ import annotations
from dataclasses import dataclass
from typing import Any
import plotext
from gtop.collector import CollectedGpuMetrics, CollectedGpuMetricsBuffer
from gtop.config import Config

PlotHandle = Any


@dataclass
class PlotextVisualizer:
    plt: PlotHandle = plotext

    def show(
        self,
        inputs: CollectedGpuMetricsBuffer,
        cfg: Config,
    ) -> None:
        plt = self.plt
        plt.clt()
        plt.cld()
        plt.plotsize(cfg.visualizer_plot_size)
        plt.theme(cfg.visualizer_plot_theme)
        plt.subplots(2, 2)
        plt.subplot(1, 1)
        self._show_gpu_info(inputs.last, plt)
        plt.subplot(1, 2)
        self._plot_utilization(inputs, plt, cfg)
        # self._bar_plot_utilization(inputs.last, plt)
        plt.subplot(2, 1)
        self._show_processes(inputs.last, plt)
        plt.subplot(2, 2)
        self._plot_pci_throughput(inputs, plt, cfg)
        # self._bar_plot_pci_throughput(inputs.last, plt)
        plt.show()

    @classmethod
    def _show_gpu_info(
        cls,
        metrics: CollectedGpuMetrics,
        plt: PlotHandle,
    ) -> None:
        gpu_info = (
            f"{metrics.name}"
            f"\nTotal Memory: {metrics.memory_total:0.0f} (MB)"
            f"\nTemperature: {metrics.temperature:0.1f} (°C)"
        ) + (
            f"\nPower Usage: {metrics.power_usage:0.1f} (W)"
            if metrics.power_usage is not None
            else ""
        )
        plt.text(gpu_info, 0, 1)
        plt.xticks([])
        plt.yticks([])
        plt.ylim(0, 1)
        # plt.title("GPU Status")
        # plt.xaxes(False, False)
        # plt.yaxes(False, False)

    @classmethod
    def _show_processes(
        cls,
        metrics: CollectedGpuMetrics,
        plt: PlotHandle,
    ) -> None:
        processes = (
            metrics.processes if metrics.processes else "No Compute Running Processes"
        )
        plt.text(processes, 0, 1)
        plt.xticks([])
        plt.yticks([])
        plt.ylim(0, 1)
        plt.title("GPU Processes")
        # plt.xaxes(False, False)
        # plt.yaxes(False, False)

    @classmethod
    def _bar_plot_pci_throughput(
        cls,
        metrics: CollectedGpuMetrics,
        plt: PlotHandle,
    ) -> None:
        names = [
            "PCI-TX",
            "PCI-RX",
        ]
        values = [
            metrics.pci_rx,
            metrics.pci_tx,
        ]
        plt.bar(
            names,
            values,
            orientation="h",
            width=2 / 5,
        )
        plt.title("GPU PCIe Throughput (MB/s)")
        plt.xlim(0, max(1, max(metrics.pci_tx, metrics.pci_rx) * 1.2))

    @classmethod
    def _bar_plot_utilization(
        cls,
        metrics: CollectedGpuMetrics,
        plt: PlotHandle,
    ) -> None:
        names = [
            "Memory",
            "Utilization",
        ]
        values = [
            metrics.memory,
            metrics.utilization,
        ]
        plt.bar(
            names,
            values,
            orientation="h",
            width=2 / 5,
        )
        plt.title("GPU Utilization (%)")
        plt.xlim(0, 100)

    @classmethod
    def _plot_pci_throughput(
        cls,
        inputs: CollectedGpuMetricsBuffer,
        plt: PlotHandle,
        cfg: Config,
    ) -> None:
        timestamps = [input.timestamp for input in inputs]
        pci_rx_values = [input.pci_rx for input in inputs]
        pci_tx_values = [input.pci_tx for input in inputs]
        plt.plot(
            timestamps,
            pci_rx_values,
            label="PCI-RX",
            marker=cfg.visualizer_plot_marker,
        )
        plt.plot(
            timestamps,
            pci_tx_values,
            label="PCI-TX",
            marker=cfg.visualizer_plot_marker,
        )
        plt.title("GPU PCIe Throughput")
        plt.xlabel("Time (s)")
        plt.ylabel("Throughput (MB/s)")
        plt.ylim(0, max(1, max(pci_tx_values + pci_rx_values) * 1.2))

    @classmethod
    def _plot_utilization(
        cls,
        inputs: CollectedGpuMetricsBuffer,
        plt: PlotHandle,
        cfg: Config,
    ) -> None:
        timestamps = [input.timestamp for input in inputs]
        utilization_values = [input.utilization for input in inputs]
        memory_values = [input.memory for input in inputs]
        plt.plot(
            timestamps,
            utilization_values,
            label="Utilization",
            marker=cfg.visualizer_plot_marker,
        )
        plt.plot(
            timestamps,
            memory_values,
            label="Memory",
            marker=cfg.visualizer_plot_marker,
        )
        # plt.title("GPU Utilization")
        plt.xlabel("Time (s)")
        plt.ylabel("Utilization (%)")
        plt.ylim(0, 100)


def show_textmode(
    inputs: CollectedGpuMetricsBuffer,
) -> None:
    print(inputs.last)
