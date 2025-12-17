\"\"\"Micro-Challenge: Cleanup Crew
Use finally for guaranteed execution.
\"\"\"
try:
    print(100 / 0)
except ZeroDivisionError:
    print("Division failed")
finally:
    print("Execution Complete - cleanup done")
