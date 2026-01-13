class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other):
        # Allow comparing two User objects by ID
        if isinstance(other, User):
            return self.id == other.id
        return False

# Testing
u1 = User(1, "Alice")
u2 = User(1, "Alice Clone")

print(u1 == u2) # True (because IDs match)
print(u1 is u2) # False (different memory addresses)
