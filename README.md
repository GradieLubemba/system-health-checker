# System Health Checker

A simple Python tool that monitors basic computer system resources and provides a quick health status.

## Features

- Displays computer name
- Detects the operating system
- Monitors CPU usage
- Monitors memory usage
- Monitors disk usage
- Provides a system health status

## Technologies

- Python
- psutil

## How to Run

### 1. Install psutil

```bash
pip install psutil
```

### 2. Run the program

```bash
python health_checker.py
```

## Example Output

```text
========================================
       SYSTEM HEALTH CHECK
========================================
Computer: DESKTOP-XXXXX
Operating System: Windows 11

--- SYSTEM RESOURCES ---
CPU Usage: 24.7%
Memory Usage: 93.2%
Disk Usage: 15.7%

--- STATUS ---
System Status: ATTENTION NEEDED
```

## What I Learned

- How to use Python to interact with system information
- How to monitor CPU, memory, and disk usage
- How to use the `psutil` library
- How to create a simple system monitoring tool
- How to document a technical project

## Future Improvements

- Add network status monitoring
- Add battery information
- Save health reports to a file
- Add warnings for high CPU or memory usage
- Create a graphical user interface

## Author

Gradie Lubemba

Computer Science Student | IT Support & Technical Troubleshooting