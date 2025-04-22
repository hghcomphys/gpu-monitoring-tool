# GPU Monitoring Tool
=====================

A lightweight CLI tool to monitor GPU performance.

## Motivation
-------------

Current GPU monitoring tools often fall short in two key areas:

* **Lack of PCI throughput metrics**: RX and TX metrics are crucial, as data transfer between CPU and GPU is frequently the computational bottleneck.
* **Inflexible metric selection**: Users should be able to customize which metrics they need to measure, rather than being limited to predefined sets.

## Intended Features
-------------------
The following features are planned for this tool:

* **Lightweight and minimal dependencies**: Easy to install and run with minimal system impact.
* **Basic metrics**: GPU utilization, Memory usage, PCI throughput, and Processes. 
* **Nvidia GPU support**: Initially targeting Nvidia GPUs, with potential expansion to AMD in the future.
* **Multi-GPU support**: Ability to monitor multiple GPUs. 
* **Customization**: support for user-level configurable file 

## Installation
------------

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

## Example Usage
---------------
A screenshot of `gtop` in action is shown below:

<img src="docs/images/screenshot.png" alt="demo screemshot" width="700"/>

### Text-mode
```bash
ghorbanh@sasdsnode01:~$ gtop -t
CollectedMetrics(timestamp=0.1, pci_tx=0.0009765625, pci_rx=0.0, process=0, memory=3.2519531249999996)
CollectedMetrics(timestamp=1.0479564666748047, pci_tx=0.0, pci_rx=0.0, process=0, memory=3.2519531249999996)
...
CollectedMetrics(timestamp=18.835940837860107, pci_tx=0.0, pci_rx=0.0, process=100, memory=4.287109375)
CollectedMetrics(timestamp=19.88008189201355, pci_tx=0.0, pci_rx=0.0009765625, process=100, memory=4.287109375)
```
