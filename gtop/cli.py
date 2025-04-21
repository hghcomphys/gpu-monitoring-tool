import pynvml
import plotext as plt
import time

from gtop.device import get_device
from gtop.metrics import Metrics
from gtop.visualize import visualize
from gtop.collect import collect


def main():

    interval = 1.0
    max_points = 30
    handle = get_device()
    metrics = Metrics()
    start_time = time.time()
    try:
        while True:
            collect(handle, metrics, start_time, max_points)
            visualize(plt, metrics)
            time.sleep(interval)
    except KeyboardInterrupt:
        # print("\nInterrupted by user.")
        pass

    finally:
        pynvml.nvmlShutdown()
