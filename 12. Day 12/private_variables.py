class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Private variable

# Testing
user = User("Eve", "secret123")

try:
    print(user.__password)
except AttributeError:
    print("Cannot access private variable __password directly")

# Accessing via name mangling (for education purposes only)
print(f"Accessed via name mangling: {user._User__password}")
