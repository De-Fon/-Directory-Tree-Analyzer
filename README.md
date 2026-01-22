# Directory Tree Analyzer

A Python utility to analyze directory structures and calculate statistics about files and folders.

## Features

- **Command-line Interface**: Pass a directory path as an argument
- **Modern pathlib Usage**: Uses `pathlib.Path` for clean path handling
- **File & Folder Counting**: Reports total files and subdirectories
- **Human-Readable Sizes**: Displays file sizes in B, KB, MB, or GB
- **Error Handling**: Validates paths and skips inaccessible files
- **Recursive Scanning**: Traverses all subdirectories

## Requirements

- Python 3.6+

## Usage

```bash
python directory_analyser.py <path>
```

### Example

```bash
python directory_analyser.py /home/user/Documents
```

### Output

```
Directory Analysis of 'Documents':
Total size: 150.75 MB
Total files: 42
Total directories: 8
```

## How It Works

1. Accepts a directory path as a command-line argument
2. Validates that the path exists and is a directory
3. Recursively walks through all subdirectories using `rglob("*")`
4. Counts files and directories, summing total file sizes
5. Handles permission errors gracefully
6. Formats sizes into human-readable units (B, KB, MB, GB)
7. Displays the analysis results

## File Structure

```
.
├── directory_analyser.py    # Main script
└── README.md               # This file
```

## License

This project is open source and available for personal and educational use.


