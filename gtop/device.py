import pynvml
import sys

DeviceHandle = pynvml.nvml.struct_c_nvmlDevice_t

def get_device(index: int = 0) -> DeviceHandle:
    try:
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(index)
    except pynvml.NVMLError as error:
        print(f"Nvidia GPU not detected! ({error})")
        sys.exit(1)
    return handle
