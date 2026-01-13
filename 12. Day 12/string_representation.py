class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"

    def __repr__(self):
        return f"User(name='{self.name}')"

# Testing
user = User("Bob")
print(str(user))  # Uses __str__
print(repr(user)) # Uses __repr__
