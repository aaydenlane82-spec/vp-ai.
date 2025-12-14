# vp.py
import time
from memory import MemoryManager
from jarvis_core import JarvisCore
from auto_upgrade import AutoUpgrade
from self_heal import SelfHeal
from error_handler import ErrorHandler

def main():
    print("VP AI starting...")
    
    # Initialize core systems
    memory = MemoryManager()
    core = JarvisCore(memory)
    upgrader = AutoUpgrade(core)
    healer = SelfHeal(core)
    error_handler = ErrorHandler(core)
    
    # Main loop
    try:
        while True:
            core.run_cycle()
            upgrader.check_for_updates()
            healer.self_repair()
            error_handler.monitor()
            time.sleep(1)
    except KeyboardInterrupt:
        print("VP AI shutting down...")

if __name__ == "__main__":
    main()
