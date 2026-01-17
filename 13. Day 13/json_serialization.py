"""
13.5 Micro-Challenge: JSON Serialization

Goal: Save a dictionary to a file.
Deep Dive: json.dump(). JSON is the standard for data exchange.
Note: JSON keys must be strings; Python allows integers, but JSON converts them.
"""
import json

def json_demo():
    filename = "data.json"
    
    # Python Dictionary with mixed key types
    data = {
        "name": "Alice",
        "age": 30,
        100: "Numeric Key",  # JSON forces keys to be strings
        "is_student": False,
        "grades": [95, 88, 92]
    }
    
    print(f"Original Python Dict: {data}")

    # Serialization: Python -> JSON File
    print(f"\nSerializing to '{filename}'...")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    # Deserialization: JSON File -> Python
    print("Deserializing back to Python...")
    with open(filename, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    
    print(f"Loaded Data: {loaded_data}")
    
    # Demonstrate key conversion
    print(f"\nKey Check: Original key 100 type: {type(100)}")
    # In loaded_data, the key '100' is now a string!
    # Note: We need to iterate to find it because direct lookup might fail if we expect int
    keys = list(loaded_data.keys())
    print(f"Loaded keys: {keys}")
    if "100" in loaded_data:
        print("Observation: Integer key 100 was converted to string '100'.")

if __name__ == "__main__":
    json_demo()
