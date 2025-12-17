\"\"\"Micro-Challenge: Pure Return
Function prints sum but returns nothing → None.
\"\"\"
def add_and_print(a, b):
    print(a + b)
    # No return → implicit return None

result = add_and_print(5, 5)
print(f"Returned value: {result}")  # None
