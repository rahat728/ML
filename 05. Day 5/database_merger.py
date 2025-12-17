\"\"\"Micro-Challenge: Database Merger
Merge two dicts with user preferences overriding defaults.
\"\"\"
defaults = {"theme": "light", "audio": "on"}
user_pref = {"theme": "dark"}

merged = defaults | user_pref  # Python 3.9+ merge operator
# merged = defaults.copy(); merged.update(user_pref)  # Alternative

print(merged)  # {'theme': 'dark', 'audio': 'on'}
