from pathlib import Path

dir_path = Path("sample_data")

file_count = 0
extension_count = {}
total_size = 0

if dir_path.exists():
    print("Path exists")
    if dir_path.is_dir():
        print("This is a directory")
        for item in dir_path.rglob("*"):
            if item.is_file():
                file_size = item.stat().st_size
                print(f"{item} - {file_size} bytes")
                file_count += 1
                total_size += file_size
                extension = item.suffix
                if extension in extension_count:
                    extension_count[extension] += 1
                else:
                    extension_count[extension] = 1
    print(f"Total files: {file_count}")
    print(f"Total size: {total_size} bytes")
    print("File extension counts:")
    for ext, count in extension_count.items():
        print(f"{ext}: {count}")
else:
    print("Path does not exist")