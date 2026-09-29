from pathlib import Path

dirPath = Path("sample_data")

file_count = 0

if dirPath.exists():
    print("Path exists")
    if dirPath.is_dir():
        print("This is a directory")
        for item in dirPath.rglob("*"):
            if item.is_file():
                print(item)
                file_count += 1
    print(f"Total files: {file_count}")
else:
    print("Path does not exist")