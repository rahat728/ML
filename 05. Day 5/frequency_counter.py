\"\"\"Micro-Challenge: Frequency Counter
Count letters in 'banana' using dict and loop.
\"\"\"
word = "banana"
freq = {}

for char in word:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)  # {'b': 1, 'a': 3, 'n': 2}
