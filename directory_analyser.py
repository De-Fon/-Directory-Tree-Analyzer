from pathlib import Path
import sys


def format_size(size):
    units = ["B", "KB", "MB", "GB"]
    index = 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    return f"{size:.2f} {units[index]}"


def analyze_directory(path):
    if not path.exists():
        print(f"Error: The path '{path}' does not exist.")
        return

    if not path.is_dir():
        print(f"Error: The path '{path}' is not a directory.")
        return


    total_size = 0
    file_count = 0
    dir_count = 0

    for item in path.rglob("*"):
        try:
            if item.is_dir():
                dir_count += 1
            elif item.is_file():
                file_count += 1
                total_size += item.stat().st_size
        except PermissionError:
            continue

    print(f"\nDirectory Analysis of '{path.name}':")
    print(f"Total size: {format_size(total_size)}")
    print(f"Total files: {file_count}")
    print(f"Total directories: {dir_count}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python directory_analyser.py <path>")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    analyze_directory(path)


