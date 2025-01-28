# ssh-failed-log-parser

## Description
A Python script to parse a log file (e.g., `auth.log`) and extract lines containing failed SSH password attempts.

## Features
- Reads log files line by line.
- Filters lines with the keyword **"Failed password"**.
- Displays all extracted log entries.

## Prerequisites
- Python 3.x installed.
- Access to an SSH authentication log file (e.g., `auth.log`).

## How to Use
1. Save the script to a file (e.g., `log_parser.py`).
2. Open your terminal or command prompt.
3. Run the script using:
   ```bash
   python log_parser.py
