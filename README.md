# EpochMonitor ⏱️

[![PyPI version](https://badge.fury.io/py/epochmonitor.svg)](https://badge.fury.io/py/epochmonitor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, lightweight, and versatile profiler for monitoring your machine learning training loops. `EpochMonitor` helps you track training time, CPU/RAM usage, and NVIDIA GPU memory usage with minimal code changes.

Get crucial insights into your model's performance and resource consumption, all presented with a clean, dynamic progress bar.

[Image of a dynamic terminal progress bar]

---

## ✨ Features

- **Easy Integration**: Use it as a simple function decorator or a flexible context manager.
- **Comprehensive Metrics**: Tracks epoch duration, total training time, CPU utilization, and RAM usage (in % and MB).
- **NVIDIA GPU Support**: Automatically detects NVIDIA GPUs and monitors memory usage per epoch.
- **Dynamic Display**: Uses `tqdm` to provide a clean, non-disruptive progress bar that updates in place.
- **Flexible Logging**: Automatically saves a detailed history of all metrics to a CSV or JSON file for later analysis.
- **Multi-GPU Aware**: Allows you to specify which GPU to monitor on systems with multiple cards.

---

## ⚙️ Installation

You can install `EpochMonitor` directly from PyPI:

```bash
pip install epochmonitor