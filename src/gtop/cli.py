import argparse
import time
from gtop.collector import CollectedGpuMetricsBuffer, collect
from gtop.config import Config
from gtop.device import free_device, get_device
from gtop.metrics import GpuMetrics
from gtop.visualizer import PlotextVisualizer, textmode_show


def parse_arguments():
    parser = argparse.ArgumentParser(description="A basic CLI tool to Monitor GPU.")
    parser.add_argument(
        "--device-gpu-index",
        "-d",
        type=int,
        default=0,
        help="GPU index to monitor (default: 0)",
    )
    parser.add_argument(
        "--update-time-interval",
        "-u",
        type=float,
        default=1.0,
        help="Time interval between updates in seconds (default: 1.0)",
    )
    parser.add_argument(
        "--text-mode",
        "-t",
        action="store_true",
        help="Enable text mode (default: False)",
    )
    return parser.parse_args()


def main():
    cfg = Config.from_parser(args=parse_arguments())
    metrics = GpuMetrics.for_device(handle=get_device(cfg))
    buffer = CollectedGpuMetricsBuffer(max_size=cfg.collector_buffer_size)
    visualizer = PlotextVisualizer()
    start_time = time.time()
    try:
        while True:
            collected_metrics = collect(metrics, start_time, cfg)
            buffer.append(collected_metrics)
            if cfg.text_mode:
                textmode_show(buffer)
            else:
                visualizer.show(buffer, cfg)

            if len(buffer) > 1:
                time.sleep(cfg.update_time_interval)
    except KeyboardInterrupt:
        pass
    finally:
        free_device()


if __name__ == "__main__":
    main()
