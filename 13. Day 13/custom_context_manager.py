"""
13.9 Micro-Challenge: Custom Context Manager

Goal: Create a block with Timer(): that prints time taken.
Deep Dive: Implement __enter__ (start timer) and __exit__ (end timer).
"""
import time

class Timer:
    def __enter__(self):
        """Called when entering the 'with' block."""
        self.start_time = time.time()
        print("Timer started...")
        return self # Value bound to 'as var'

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting the 'with' block."""
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        print(f"Timer stopped. Duration: {duration:.4f} seconds")
        
        # If an exception happened, exc_type will not be None.
        # Returning False allows the exception to propagate.
        return False 

def heavy_computation():
    time.sleep(1) # Sleep for 1 second

if __name__ == "__main__":
    print("Measuing performance of heavy_computation()...")
    
    with Timer():
        heavy_computation()
        
    print("Done.")
