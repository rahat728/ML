\"\"\"Micro-Challenge: Input Guard
Safe integer input with ValueError handling.
\"\"\"
while True:
    try:
        age = int(input("Enter your age: "))
        print(f"Age accepted: {age}")
        break
    except ValueError:
        print("Numbers only. Please try again.")
