\"\"\"Micro-Challenge: Math Safety Net
Catch ZeroDivisionError specifically.
\"\"\"
x = 0
try:
    result = 100 / x
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
