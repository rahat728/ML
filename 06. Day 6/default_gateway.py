\"\"\"Micro-Challenge: Default Gateway
Function with default parameter.
\"\"\"
def connect(port=3306):
    print(f"Connecting to port {port}")

connect()        # Uses default → 3306
connect(5432)    # Overrides → 5432
