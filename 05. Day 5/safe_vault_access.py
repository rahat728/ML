\"\"\"Micro-Challenge: Safe Vault
Safe dictionary access using .get().
\"\"\"
user = {"id": 1}

# Direct access would crash if key missing
# email = user["email"]  # KeyError

email = user.get("email", "No Email Found")
print(f"Email: {email}")
