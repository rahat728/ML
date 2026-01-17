"""
13.6 Micro-Challenge: CSV Parsing

Goal: Read a CSV into a list of dictionaries.
Deep Dive: Use csv.DictReader.
It handles quoted strings and delimiters automatically, preventing bugs when data contains commas.
"""
import csv

def csv_demo():
    filename = "users.csv"
    
    # 1. Create a dummy CSV file manually
    # Notice the comma inside the string "New York, NY"
    csv_content = """id,name,city,role
1,Alice,"New York, NY",Engineer
2,Bob,"San Francisco, CA",Designer
3,Charlie,"London, UK",Manager
"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(csv_content)
    print(f"Created '{filename}' with quoted strings.")

    # 2. Read using csv.DictReader
    print("\nParsing with csv.DictReader...")
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        # Iterate over rows
        users = list(reader)
        
        for user in users:
            print(user)
            # Verify that "New York, NY" stayed together
            if user['name'] == 'Alice':
                print(f" -> Verified City for Alice: {user['city']}")

if __name__ == "__main__":
    csv_demo()
