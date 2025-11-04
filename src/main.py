import os
import sys
import shutil
from pathlib import Path
from textnode import *
print('hello world')

def delete_files_in_dir(directory_path):
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if os.path.isfile(filepath):
            os.remove(filepath)
            print(f"Deleted file: {filepath}")

def copy_dir_recursive(source_path, destination_path):
    if not destination_path.exists():
        destination_path.mkdir()
    for file in source_path.iterdir():
        new_file = destination_path / file.name
        if file.is_dir():
            copy_dir_recursive(file, new_file)
        else:
            print(f"Copying {file} to {new_file}")
            shutil.copy(file, new_file)

def main():
    project_root = Path(__file__).parent.parent
    destination_dir = project_root / "public"
    source_dir = project_root / "static"
    
    #remove dir before copying
    if destination_dir.exists():
        delete_files_in_dir(destination_dir)

    copy_dir_recursive(source_dir, destination_dir)


main()
