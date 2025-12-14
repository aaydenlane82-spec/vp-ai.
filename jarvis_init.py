# jarvis_init.py
from jarvis_core import JarvisCore
from memory import MemoryManager

def init_jarvis():
    memory = MemoryManager()
    core = JarvisCore(memory)
    return core
