import os
import json

FILE_PATH = "data/tickets.json"
def initialize_storage():
    if not os.path.exists("data"):
            os.mkdir("data")
            print("folder does not exist, creating data folder")
    if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'w') as f:
                json.dump([], f)

def load_tickets():
    try:
        with open(FILE_PATH, "r") as f:
             return json.load(f)
    except json.JSONDecodeError:
         print("Error: Corrupted JSON file")
    except FileNotFoundError:
        print("Error: file not found")
        return []
    
def save_tickets(tickets):
     with open(FILE_PATH, "w") as f:
          json.dump(tickets, f, indent=4)
            
            
