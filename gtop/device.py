import sys
import pynvml
from gtop.config import Config

DeviceHandle = pynvml.nvml.struct_c_nvmlDevice_t


def get_device(cfg: Config) -> DeviceHandle:
    try:
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(cfg.device_gpu_index)

    except pynvml.NVMLError as error:
        print(f"Nvidia GPU not detected! ({error})")
        sys.exit(1)
    return handle


def free_device() -> None:
    pynvml.nvmlShutdown()
