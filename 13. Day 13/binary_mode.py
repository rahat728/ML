"""
13.3 Micro-Challenge: Binary Mode

Goal: Read an image file.
Deep Dive: Use mode 'rb'.
Text modes decode bytes to String (UTF-8).
Binary modes return raw bytes, essential for images/PDFs.
"""

def create_dummy_binary_file(filename: str):
    """Creates a small binary file mimicking an image header."""
    # PNG signature: \x89PNG\r\n\x1a\n
    dummy_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'
    with open(filename, 'wb') as f:
        f.write(dummy_data)
    print(f"Created dummy binary file: {filename}")

def read_binary_file(filename: str):
    """Reads a file in binary mode to see raw bytes."""
    print(f"\nReading '{filename}' in binary mode ('rb')...")
    
    with open(filename, 'rb') as f:
        content = f.read(16) # Read first 16 bytes
        print(f"Raw Bytes: {content}")
        print(f"Hex Representation: {content.hex()}")

def fail_read_text_mode(filename: str):
    """Attempts to read binary data as text to trigger an error or garbage."""
    print(f"\nAttempting to read '{filename}' in text mode ('r')...")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"Text Content: {content}")
    except Exception as e:
        print(f"Error reading as text: {e}")

if __name__ == "__main__":
    IMG_FILE = "test_image.bin"
    create_dummy_binary_file(IMG_FILE)
    read_binary_file(IMG_FILE)
    fail_read_text_mode(IMG_FILE)
