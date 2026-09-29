from pathlib import Path

dirPath = Path("sample_data")

if dirPath.exists():
    print("Path exists")
    if dirPath.is_dir():
        print("This is a directory")
        for item in dirPath.rglob("*"):
            if item.is_file():
                print(item)
else:
    print("Path does not exist")