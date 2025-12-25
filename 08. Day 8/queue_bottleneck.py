"""
Day 8.4: The Queue Bottleneck

Goal: Compare pop() vs pop(0).
Deep Dive: pop(0) requires a Left Shift of all remaining items to fill the gap.
"""
import time
from collections import deque

def run_task():
    N = 100_000
    print(f"--- 8.4 Queue Bottleneck (N={N}) ---")

    # Setup lists
    list_end = list(range(N))
    list_start = list(range(N))
    deque_obj = deque(range(N))

    # TEST 1: Pop from End
    start = time.time()
    while list_end:
        list_end.pop()
    print(f"List .pop():     {time.time() - start:.5f} seconds (O(1))")

    # TEST 2: Deque Pop Left
    start = time.time()
    while deque_obj:
        deque_obj.popleft()
    print(f"Deque .popleft(): {time.time() - start:.5f} seconds (O(1))")

    # TEST 3: Pop from Start (The Trap)
    start = time.time()
    while list_start:
        list_start.pop(0) # Shifts all N items left
    print(f"List .pop(0):    {time.time() - start:.5f} seconds (O(N))")
    print("Conclusion: Use collections.deque for FIFO queues.\n")

if __name__ == "__main__":
    run_task()
