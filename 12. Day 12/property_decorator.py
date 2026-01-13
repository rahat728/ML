from datetime import datetime

class User:
    def __init__(self, birth_year):
        self.birth_year = birth_year

    @property
    def age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year

# Testing
user = User(1995)
print(f"Age: {user.age}")  # Accessed like a variable, but runs the method
