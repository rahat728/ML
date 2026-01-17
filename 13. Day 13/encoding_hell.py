"""
13.4 Micro-Challenge: Encoding Hell

Goal: Fix a "UnicodeDecodeError".
Deep Dive: Always specify encoding='utf-8'.
Windows defaults to 'cp1252', which crashes on emojis or foreign characters.
"""

def demonstrate_encoding_issues():
    filename = "emoji_test.txt"
    # Content with emoji (requires UTF-8)
    content = "Hello World! 🌍🚀"

    # 1. Write using UTF-8 (Standard)
    print("Writing UTF-8 content...")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    # 2. Try to read using ASCII (Will Fail)
    print("\nAttempting to read with 'ascii' encoding...")
    try:
        with open(filename, 'r', encoding='ascii') as f:
            print(f.read())
    except UnicodeDecodeError as e:
        print(f"❌ FAIL: {e}")
        print(" -> Explanation: ASCII cannot handle emojis (byte > 127).")

    # 3. Correctly read with UTF-8
    print("\nReading with 'utf-8' encoding...")
    with open(filename, 'r', encoding='utf-8') as f:
        print(f"✅ SUCCESS: {f.read()}")

if __name__ == "__main__":
    demonstrate_encoding_issues()
