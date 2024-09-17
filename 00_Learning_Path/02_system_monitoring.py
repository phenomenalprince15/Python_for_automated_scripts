import psutil
import time

# Monitor CpU usage
for _ in range(5):
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
