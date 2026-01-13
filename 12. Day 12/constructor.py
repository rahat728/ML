class User:
    def __init__(self):
        print("User created")
        self.is_active = True

# Testing
user = User()
print(f"Is active: {user.is_active}")
