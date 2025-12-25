"""
Day 8.3: The Insertion Trap (O(N))

Goal: Compare append vs insert(0).
Deep Dive: insert(0) forces Python to SHIFT every existing item to the right.
"""
import time

def run_task():
    N = 200_000 # Smaller N because insert(0) is very slow
    print(f"--- 8.3 Insertion Trap (N={N}) ---")

    # TEST 1: APPEND
    data_append = []
    start_append = time.time()
    for i in range(N):
        data_append.append(i) # O(1)
    end_append = time.time()
    print(f"Append time:   {end_append - start_append:.5f} seconds (Fast)")

    # TEST 2: INSERT(0)
    data_insert = []
    start_insert = time.time()
    for i in range(N):
        data_insert.insert(0, i) # O(N) - shifts memory every single time
    end_insert = time.time()
    print(f"Insert(0) time: {end_insert - start_insert:.5f} seconds (Slow)")
    
    print("Conclusion: Never use insert(0) in a loop on large lists.\n")

if __name__ == "__main__":
    run_task()
