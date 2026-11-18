# File & Folder Inventory Reporter

A beginner Python scripting project that scans a directory and generates a simple file inventory report.

## Features

- Recursively scans a directory
- Counts total files
- Counts files by extension
- Calculates total directory size
- Displays file sizes
- Identifies the three largest files
- Accepts a directory path through the command line
- Handles invalid paths and basic filesystem access errors

## Usage

Run the script with:

```bash
python inventory.py --path <directory>
```

Example:

```bash
python inventory.py --path sample_data
```

View command-line help with:

```bash
python inventory.py --help
```

## Example Output

```text
Contents of directory: sample_data
sample_data/notes.txt - 22 bytes
sample_data/report.txt - 28 bytes

Total files: 8
Total size: 245 bytes

Largest files:
sample_data/users.csv - 70 bytes
sample_data/logs/auth.log - 55 bytes
sample_data/config.json - 40 bytes

File extension counts:
.txt: 3
.csv: 1
.json: 1
.log: 2
.md: 1
```

## Python Concepts Practiced

- Variables and control flow
- Loops and conditions
- Lists, tuples, and dictionaries
- Functions and return values
- Sorting with `sorted()`
- Exception handling
- Command-line arguments with `argparse`
- Filesystem operations with `pathlib`
- Basic program structure with `main()`

## Project Purpose

This project was built as part of my Python scripting and security automation learning roadmap.

The main goal was to practice the core automation pattern:

```text
Input → Process → Output
```

and learn how to work with filesystem data in Python.

## Project Classification

Learning project / beginner GitHub project.

The main value of this project is demonstrating Python scripting fundamentals rather than acting as a production-ready security tool.