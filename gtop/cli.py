import argparse
import time

import plotext as plt

from gtop.collector import collect
from gtop.config import Config
from gtop.device import free_device, get_device
from gtop.metrics import Metrics
from gtop.visualizer import visualize


def parse_arguments():
    parser = argparse.ArgumentParser(description="A basic CLI tool to Monitor GPU.")
    parser.add_argument(
        "--update-interval",
        "-i",
        type=float,
        default=1.0,
        help="Time interval between updates in seconds (default: 1.0)",
    )
    parser.add_argument(
        "--device-gpu-index",
        "-g",
        type=int,
        default=0,
        help="GPU index to monitor (default: 0)",
    )
    parser.add_argument(
        "--collector-max-points",
        "-p",
        type=int,
        default=30,
        help="Maximum number of data points shown in graphs (default: 30)",
    )
    return parser.parse_args()


def main():

    cfg = Config.from_parser(args=parse_arguments())
    handle = get_device(cfg)
    metrics = Metrics()
    start_time = time.time()
    try:
        while True:
            collect(metrics, handle, start_time, cfg)
            visualize(metrics, plt, cfg)
            time.sleep(cfg.update_interval)
    except KeyboardInterrupt:
        pass

    finally:
        free_device()


if __name__ == "__main__":
    main()
