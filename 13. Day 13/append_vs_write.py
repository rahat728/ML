"""
13.2 Micro-Challenge: Append vs Write

Goal: Add a log line to a file without deleting old content.
Deep Dive:
- Mode 'w' wipes the file.
- Mode 'a' appends to the end.
- Mode 'x' fails if file exists (Safety).
"""
import os

def demonstrate_modes(filename: str) -> None:
    # 1. Mode 'w': Write (Overwrites existing content)
    print("--- Mode 'w' (Write) ---")
    with open(filename, 'w') as f:
        f.write("Line 1: Initial content.\n")
    print(f"Created '{filename}' with initial content.")

    # 2. Mode 'a': Append (Adds to the end)
    print("\n--- Mode 'a' (Append) ---")
    with open(filename, 'a') as f:
        f.write("Line 2: Appended content.\n")
    print("Appended a new line.")

    # Verify content
    with open(filename, 'r') as f:
        print("\nCurrent File Content:")
        print(f.read())

    # 3. Mode 'x': Exclusive Creation (Fails if exists)
    print("--- Mode 'x' (Exclusive Create) ---")
    try:
        with open(filename, 'x') as f:
            f.write("This shouldn't be written.")
    except FileExistsError:
        print(f"Safety Check: Failed to open '{filename}' in 'x' mode as it already exists.")

if __name__ == "__main__":
    FILENAME = "mode_demo.txt"
    if os.path.exists(FILENAME):
        os.remove(FILENAME) # Clean slate
    demonstrate_modes(FILENAME)
