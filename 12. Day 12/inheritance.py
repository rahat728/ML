class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        print(f"{self.name} logged in")

class Admin(User):
    def delete_db(self):
        print("Database deleted! (Admin only)")

# Testing
user = User("Standard User")
admin = Admin("Super Admin")

user.login()
admin.login() # Admin inherits login

admin.delete_db()
try:
    user.delete_db()
except AttributeError:
    print("Standard users cannot delete the DB")
