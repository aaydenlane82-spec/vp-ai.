# self_heal.py
import time
import traceback

class SelfHeal:
    def __init__(self, core):
        self.core = core

    def self_repair(self):
        try:
            self.core.check_integrity()
        except Exception as e:
            print(f"Self-Heal detected issue: {e}")
            traceback.print_exc()
            self.core.reboot_module()
