raw_input = input("Enter a number: ")
print(f"Type of raw input: {type(raw_input)}")
try:
    num = float(raw_input)
    print(f"Type after casting: {type(num)}")
except ValueError:
    print("Invalid input, cannot cast to float.")
