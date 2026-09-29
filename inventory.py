from pathlib import Path

dirPath = Path("sample_data")

file_count = 0
extension_count = {}

if dirPath.exists():
    print("Path exists")
    if dirPath.is_dir():
        print("This is a directory")
        for item in dirPath.rglob("*"):
            if item.is_file():
                print(item)
                file_count += 1
                extension = item.suffix
                if extension in extension_count:
                    extension_count[extension] += 1
                else:
                    extension_count[extension] = 1
    print(f"Total files: {file_count}")
    print("File extension counts:")
    for ext, count in extension_count.items():
        print(f"{ext}: {count}")
else:
    print("Path does not exist")