# GPU Monitoring Tool
A lightweight CLI tool to monitor GPU performance.

## Motivation
Current GPU monitoring tools often fall short in two key areas:

* Lack of PCI throughput metrics: RX and TX metrics are important, as data transfer between CPU and GPU is frequently the computational bottleneck.
* Inflexible metric selection: Users should be able to customize which metrics they need to measure, rather than being limited to predefined sets.

## Features (intended)
The following features are planned for this tool:

* Lightweight and minimal
* Basic metrics like GPU utilization, memory usage, PCI throughput, and processes. 
* Support monitoring multiple GPUs. 
* Targeting Nvidia GPUs, with potential extension to AMD GPUs.
* User-level customizations 

## Installation
To install `gtop`, run the following command:
```bash
pip install --user .
```
This will install required dependencies and add `gtop` to your user-specific executable path (`~/.local/bin`). 
You can then run `gtop` directly.

To uninstall `gtop`, use the following command:
```bash
pip uninstall gtop
```

## Examples
A screenshot of `gtop` in action is shown below:

<img src="docs/images/screenshot.png" alt="demo screemshot" width="700"/>

### Text-mode
Text mode can be enabled via `--text-mode` or `-t` flag:
```bash
$ gtop -t

CollectedMetrics(timestamp=0.1, pci_tx=0.0009765625, pci_rx=0.0, process=0, memory=3.2519531249999996)
CollectedMetrics(timestamp=1.0479564666748047, pci_tx=0.0, pci_rx=0.0, process=0, memory=3.2519531249999996)
...
CollectedMetrics(timestamp=18.835940837860107, pci_tx=0.0, pci_rx=0.0, process=100, memory=4.287109375)
CollectedMetrics(timestamp=19.88008189201355, pci_tx=0.0, pci_rx=0.0009765625, process=100, memory=4.287109375)
```