# GPU Monitoring Tool

<!-- [![PyPI](https://img.shields.io/pypi/v/gtop?label=pypi%20package)](https://pypi.org/project/gtop) -->
<!-- [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) -->

A lightweight CLI tool to monitor GPU status.

<!--
## Motivation
Current GPU monitoring tools often fall short in two ways:

* Inflexible metric selection: users should be able to customize which metrics they need to measure, rather than being limited to predefined sets.
* No PCI throughput metrics: RX and TX metrics are important, as data transfer between CPU and GPU is frequently the computational bottleneck.
-->

<!--
## Features
The following features are planned for this tool:

[x] Basic metrics like GPU utilization, memory usage, PCI throughput
[x] Targeting Nvidia GPUs, with potential extension to AMD GPUs
* A table of GPU processes
* User-level customization 
* Lightweight and minimal
* Multiple GPU support 
-->

## Installation
To install `gtop`, run the following command:
```bash
pip install --user git+https://github.com/hghcomphys/gpu-monitoring-tool.git
```
This will install required dependencies and add `gtop` to your user-specific executable path (`~/.local/bin`). 
You can then run `gtop` directly.

To uninstall `gtop`, use the following command:
```bash
pip uninstall gtop
```

## Example
A screenshot of `gtop` in action is shown below:

<img src="docs/images/screenshot.png" alt="demo screemshot" width="700"/>

### Text-mode
Text mode can be enabled via `--text-mode` or `-t` flag:
```bash
$ gtop -t
CollectedMetrics(Time=0.10(s), Process=0.00(%), Memory=2.31(%), PCI-RX=0.00(MB/s), PCI-TX=0.00(MB/s))
CollectedMetrics(Time=1.13(s), Process=0.00(%), Memory=2.31(%), PCI-RX=0.00(MB/s), PCI-TX=0.00(MB/s))
...
CollectedMetrics(Time=10.14(s), Process=100.00(%), Memory=3.74(%),  PCI-RX=42.37(MB/s), PCI-TX=0.01(MB/s))
CollectedMetrics(Time=11.18(s),  Process=100.00(%), Memory=3.74(%), PCI-RX=0.03(MB/s), PCI-TX=11.02(MB/s))
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
