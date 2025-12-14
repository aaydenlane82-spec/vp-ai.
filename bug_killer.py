# bug_killer.py
import subprocess
import sys
import os

SCRIPTS = ["vp.py", "auto_upgrade.py", "self_heal.py"]

def run():
    for s in SCRIPTS:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), s)
        try:
            subprocess.run([sys.executable, path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"{s} crashed with code {e.returncode}, restarting...")
        except Exception as e:
            print(f"{s} unexpected error: {e}")

if __name__ == "__main__":
    run()
