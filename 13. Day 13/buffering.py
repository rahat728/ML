"""
13.7 Micro-Challenge: Buffering

Goal: Write 1 million lines. Why doesn't the disk spin 1 million times?
Deep Dive: Python (and the OS) uses a **Buffer**.
Data accumulates in RAM and is "Flushed" to disk in chunks to save I/O cycles.
"""
import time
import os

def buffering_demo():
    filename = "large_file.txt"
    count = 1_000_000
    
    print(f"Writing {count} lines to '{filename}'...")
    start_time = time.time()
    
    with open(filename, 'w') as f:
        for i in range(count):
            f.write(f"Line {i}: This is some sample text to fill the buffer.\n")
            

    end_time = time.time()
    
    duration = end_time - start_time
    file_size_mb = os.path.getsize(filename) / (1024 * 1024)
    
    print(f"\nDone! Written {file_size_mb:.2f} MB.")
    print(f"Time Taken: {duration:.4f} seconds.")
    print("Observation: The speed is high because disk I/O happens in large chunks (buffered), not line-by-line.")
    
    # Cleanup big file
    os.remove(filename)
    print("Cleaned up large file.")

if __name__ == "__main__":
    buffering_demo()
