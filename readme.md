# GPU Monitoring Tool
A basic CLI tool to monitor code performance on GPU. 

## Why?
It would be quite useful when optimizing GPU-accelerated computing.
Most of current GPU monitoring tools don't support PCI throughput/bandwidth. 
These metrics are important to be measured as most of the time data transfer between CPU and GPU is the computational bottleneck.  

## Intended Features:
- lightweight and minimal (dependencies)
- GPU utilization, memory usage, PCI throughput
- works on Nvidia GPU (for now)
- support for multiple GPUs


