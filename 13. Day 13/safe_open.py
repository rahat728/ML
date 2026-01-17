"""
13.1 Micro-Challenge: The Safe Open

Goal: Write to a file without .close().
Deep Dive: Use with open(...) as f. This is a Context Manager.
It guarantees file closure even if an exception crashes the block.
"""

def safe_file_write(filename: str, content: str) -> None:
    """
    Writes content to a file using a context manager.
    
    The 'with' statement ensures that f.close() is called automatically,
    even if an error occurs inside the block.
    """
    print(f"Opening '{filename}' safely...")
    
    # Context manager opens the file and assigns it to 'f'
    with open(filename, 'w') as f:
        f.write(content)
        print("Write successful.")
        
        # Simulating a potential crash to prove safety?
        # raise ValueError("Oops! Something went wrong inside the block.")
    
    print(f"File '{filename}' is closed automatically.")

if __name__ == "__main__":
    try:
        safe_file_write("safe_open.txt", "This file was opened and closed safely!\nNo .close() needed.")
    except Exception as e:
        print(f"Caught exception: {e}")
