class User:
    def __init__(self, name):
        self.name = name
        print(f"User {name} initialized")

class Admin(User):
    def __init__(self, name, level):
        super().__init__(name) # Calls User.__init__
        self.level = level
        print(f"Admin level {level} initialized")

# Testing
admin = Admin("Boss", "Top Tier")
print(f"Admin: {admin.name}, Level: {admin.level}")
