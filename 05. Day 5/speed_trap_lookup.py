\"\"\"Micro-Challenge: Speed Trap (Lookup)
Demonstrate O(1) vs O(N) lookup with list vs set/dict.
\"\"\"
# Simulate large collection concept (actual 1M not needed)
numbers_list = list(range(10000))
numbers_set = set(numbers_list)

# Lookup performance difference explanation in comments
print("List lookup requires scanning, O(N)")
print("Set/Dict lookup uses hash, O(1) - instant even for millions")
print("Example check:")
print(-1 in numbers_list)  # False (scans)
print(-1 in numbers_set)   # False (instant)
