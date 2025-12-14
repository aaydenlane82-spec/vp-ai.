# jarvis_runtime.py
from jarvis_core import JarvisCore

class JarvisRuntime:
    def __init__(self, core):
        self.core = core

    def run(self):
        self.core.run_cycle()
