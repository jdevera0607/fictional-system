import os
import json

class Storage:
    def __init__(self, file_path):
         self.file_path = file_path

    def initialize_storage(self):
        directory = os.path.dirname(self.file_path)

        if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)

        if not os.path.exists(self.file_path):
                with open(self.file_path, 'w') as f:
                    json.dump([], f)

    def load_tickets(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            raise Exception("JSON is corrupted")

        except FileNotFoundError:
            raise Exception("File not found")
        
    def save_tickets(self, tickets):
        with open(self.file_path, "w") as f:
            json.dump(tickets, f, indent=4)
                
storage = Storage("data/tickets.json")