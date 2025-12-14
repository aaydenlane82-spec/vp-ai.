# upgrades.py
import json
import os

class Upgrades:
    def __init__(self, path="upgrades.json"):
        self.path = path
        self.load_upgrades()

    def load_upgrades(self):
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump([], f)
        with open(self.path, "r") as f:
            self.upgrades = json.load(f)

    def get_pending(self):
        return [u for u in self.upgrades if not u.get("applied", False)]

    def mark_applied(self, upgrade):
        upgrade["applied"] = True
        self.save()

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.upgrades, f, indent=4)
