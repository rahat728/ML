"""
13.8 Micro-Challenge: Pathlib

Goal: Join a folder and filename safely on Windows and Mac.
Deep Dive: Do not use string concatenation folder + "/" + file.
Use pathlib.Path. It handles OS-specific separators (\ vs /) automatically.
"""
from pathlib import Path
import os

def pathlib_demo():
    # 1. Create a Path object for the current directory
    current_dir = Path.cwd()
    print(f"Current Directory: {current_dir}")
    
    # 2. Construct a path safely (OS agnostic)
    # This works on both Windows (\) and Linux/Mac (/)
    new_folder = current_dir / "my_folder" / "subfolder"
    filename = new_folder / "config.txt"
    
    print(f"Constructed Path: {filename}")
    
    # 3. Create the directory structure if it doesn't exist
    # parents=True creates missing parent dirs, exist_ok=True ignores if exists
    new_folder.mkdir(parents=True, exist_ok=True)
    print("Created directory structure verified.")
    
    # 4. Write to file using Path object directly
    filename.write_text("Hello from Pathlib!", encoding='utf-8')
    print("Written to file via Path object.")
    
    # 5. Read from file
    content = filename.read_text(encoding='utf-8')
    print(f"Read Content: {content}")
    
    # Cleanup
    filename.unlink()
    try:
        new_folder.rmdir()
        new_folder.parent.rmdir()
    except OSError:
        pass # Directory might not be empty or other issues
    print("Cleanup complete.")

if __name__ == "__main__":
    pathlib_demo()
