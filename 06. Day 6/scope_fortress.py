\"\"\"Micro-Challenge: Scope Fortress
Show local vs global variable behavior.
\"\"\"
x = 10  # Global

def change_x():
    x = 20  # Local variable (does not affect global)
    print(f"Inside function: x = {x}")

change_x()
print(f"Outside function: x = {x}")  # Still 10
