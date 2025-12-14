# error_handler.py
import traceback
import sys

class ErrorHandler:
    def __init__(self, core):
        self.core = core

    def monitor(self):
        try:
            self.core.run_health_checks()
        except Exception as e:
            print(f"ErrorHandler caught exception: {e}")
            traceback.print_exc()
            self.core.restart_module()
