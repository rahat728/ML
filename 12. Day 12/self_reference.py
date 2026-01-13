class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        # self is the instance calling this method
        print(f"{self.name} is logging in")

# Testing
user = User("Alice")
user.login() 
# Python converts this to: User.login(user)
