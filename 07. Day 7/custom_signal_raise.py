\"\"\"Micro-Challenge: Custom Signal
Raise exception for negative input.
\"\"\"
try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise ValueError("No negatives allowed")
    print(f"Accepted: {num}")
except ValueError as e:
    print(f"Error: {e}")
