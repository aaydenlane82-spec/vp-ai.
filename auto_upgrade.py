# auto_upgrade.py
import time
import json
from upgrades import Upgrades

class AutoUpgrade:
    def __init__(self, core):
        self.core = core
        self.upgrades = Upgrades()
        self.last_check = time.time()

    def check_for_updates(self):
        current_time = time.time()
        # Check every 60 seconds
        if current_time - self.last_check > 60:
            self.last_check = current_time
            updates = self.upgrades.get_pending()
            for u in updates:
                try:
                    self.core.apply_upgrade(u)
                    print(f"Applied upgrade: {u}")
                    self.upgrades.mark_applied(u)
                except Exception as e:
                    print(f"Failed upgrade {u}: {e}")
