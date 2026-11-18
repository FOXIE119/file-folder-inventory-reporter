from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description="Scan a directory and display file inventory.")
parser.add_argument("--path", required=True, help="Path to the directory to scan")

args = parser.parse_args()

def scan_directory(path):
    file_count = 0
    total_size = 0
    extension_count = {}
    file_sizes = []
    
    for item in path.rglob("*"):
        if item.is_file():
            try:
                file_size = item.stat().st_size
            except OSError:
                print(f"Error occurred while accessing {item}")
                continue
            file_count += 1
            total_size += file_size
            file_sizes.append((item, file_size))
            extension = item.suffix
            if extension in extension_count:
                extension_count[extension] += 1
            else:
                extension_count[extension] = 1
    return file_count, total_size, extension_count, file_sizes


def display_report(file_count, total_size, extension_count, file_sizes):
    print(f"Total files: {file_count}")
    print(f"Total size: {total_size} bytes")

    sorted_file_sizes = sorted(file_sizes, key=lambda file_info: file_info[1], reverse=True)
    print("\nLargest files:")
    for item, size in sorted_file_sizes[:3]:
        print(f"{item} - {size} bytes")
    print("\nFile extension counts:")
    for ext, count in extension_count.items():
        print(f"{ext}: {count}")


def print_directory_contents(path, file_sizes):    
    print(f"Contents of directory: {path}")
    for item, size in file_sizes:
        print(f"{item} - {size} bytes")    


dir_path = Path(args.path)

if not dir_path.exists():
    print("Path does not exist")
elif not dir_path.is_dir():
    print("Path exists but is not a directory")
else:
    file_count, total_size, extension_count, file_sizes = scan_directory(dir_path)
    print_directory_contents(dir_path, file_sizes)
    display_report(file_count, total_size, extension_count, file_sizes)