# launcher.py
import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VP_PATH = os.path.join(BASE_DIR, "vp.py")

if __name__ == "__main__":
    try:
        subprocess.run([sys.executable, VP_PATH], check=True)
    except subprocess.CalledProcessError as e:
        print(f"VP exited with code {e.returncode}.")
    except KeyboardInterrupt:
        print("Launcher exiting...")
