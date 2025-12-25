"""
Day 8.9: The Dictionary Creator

Goal: Cost of building vs searching.
Deep Dive: Building is O(N) because hashes must be calculated for every item.
"""
import time

def run_task():
    N = 1_000_000
    print(f"--- 8.9 Dict Creator (N={N}) ---")
    
    data_list = list(range(N))
    
    # Measure Build Time
    start = time.time()
    my_dict = {i: i for i in data_list}
    end = time.time()
    print(f"Build Time (O(N)): {end - start:.5f} seconds")
    
    # Measure Lookup Time
    start_lookup = time.time()
    _ = my_dict[500_000]
    end_lookup = time.time()
    print(f"Lookup Time (O(1)): {end_lookup - start_lookup:.10f} seconds")
    print("Conclusion: Pay the build cost once, enjoy fast lookups forever.\n")

if __name__ == "__main__":
    run_task()
