class User:
    species = "Human"  # Class Variable (shared)

    def __init__(self, name):
        self.name = name  # Instance Variable (unique)

u1 = User("Alice")
u2 = User("Bob")

print(f"u1: {u1.name}, {u1.species}")
print(f"u2: {u2.name}, {u2.species}")

# Change class variable
User.species = "Superhuman"
print(f"After mutation -> u1: {u1.species}, u2: {u2.species}")

# Change instance variable for one
u1.species = "Cyborg" # Creates a new instance variable 'species' for u1
print(f"After instance override -> u1: {u1.species}, u2: {u2.species}")
