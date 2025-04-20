# GPU Monitoring Tool
A basic CLI tool to monitor code performance on GPU. 

## Why?
It would be quite useful when optimizing code running on the GPU.
Most current GPU monitoring tools don't show PCI throughput/bandwidth info. 
These metrics are important to be measured as most of the time data transfer between CPU and GPU is the computational bottleneck.  

## Intended Features:
- lightweight and minimal (dependencies) design
- GPU utilization, memory usage, PCI throughput
- work on Nvidia GPU (for now)
- support for multiple GPUs

## Installation
```bash
$ pip install --user .
```
This will install required dependencies and adding `gtop` to user specific executable `~/.local/bin`.
Then, simply run `gtop`.

To uninstall `gtop` use this command
```bash
$ pip uninstall gtop
```

## Screenshots
<img src="screenshot.png" alt="demo" width="700"/>
