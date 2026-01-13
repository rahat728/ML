class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        # Allow adding two Wallet objects
        return Wallet(self.amount + other.amount)

    def __str__(self):
        return f"${self.amount}"

# Testing
w1 = Wallet(100)
w2 = Wallet(50)

w3 = w1 + w2  # Python calls w1.__add__(w2)
print(f"Total: {w3}")
