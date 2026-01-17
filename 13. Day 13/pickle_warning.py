"""
13.10 Micro-Challenge: Pickle (The Warning)

Goal: Save a Python Object (Class) to file.
Deep Dive: Use pickle.
Warning: Never unpickle data from untrusted sources. It can execute arbitrary code (Security Risk).
"""
import pickle
import os

class GameState:
    def __init__(self, level: int, score: int, player: str):
        self.level = level
        self.score = score
        self.player = player
    
    def __str__(self):
        return f"Player: {self.player}, Level: {self.level}, Score: {self.score}"

def pickle_demo():
    filename = "savegame.pkl"
    
    # 1. Create a complex object
    state = GameState(level=5, score=9999, player="Raider")
    print(f"Original Object: {state}")
    
    # 2. Serialize (Pickle) to file
    print(f"Saving to '{filename}'...")
    with open(filename, 'wb') as f:
        pickle.dump(state, f)
        
    # 3. Deserialize (Unpickle) from file
    print("Loading from file...")
    with open(filename, 'rb') as f:
        loaded_state = pickle.load(f)
        
    print(f"Loaded Object:   {loaded_state}")
    
    # 4. Security Warning Demonstration
    # NEVER unpickle untrusted data! Malicious data can run code.
    # We won't demonstrate the exploit, but know that __reduce__ can be used to execute shell commands.
    
    # Cleanup
    os.remove(filename)

if __name__ == "__main__":
    pickle_demo()
