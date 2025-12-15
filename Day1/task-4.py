try:
    total_seconds = int(input("Enter total seconds: "))
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
except ValueError:
    print("Invalid input, must be an integer.")
