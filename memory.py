# memory.py
import json
import os

class MemoryManager:
    def __init__(self, path="memory.json"):
        self.path = path
        self.load()

    def load(self):
        if not os.path.exists(self.path):
            self.memory = {}
            self.save()
        else:
            with open(self.path, "r") as f:
                self.memory = json.load(f)

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.memory, f, indent=4)

    def set(self, key, value):
        self.memory[key] = value
        self.save()

    def get(self, key, default=None):
        return self.memory.get(key, default)
