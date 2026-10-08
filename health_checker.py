import platform
import psutil
from datetime import datetime


def check_system():
    print("=" * 40)
    print("       SYSTEM HEALTH CHECK")
    print("=" * 40)

    print(f"Computer: {platform.node()}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    print("\n--- SYSTEM RESOURCES ---")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    print(f"CPU Usage:    {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage:   {disk}%")

    print("\n--- STATUS ---")

    if cpu < 80 and memory < 80 and disk < 90:
        print("System Status: GOOD")
    else:
        print("System Status: ATTENTION NEEDED")


if __name__ == "__main__":
    check_system()