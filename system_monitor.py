import time
import psutil

while True:
    cpu = psutil.cpu_percent()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    print(f"CPU Usage: {cpu}% at {timestamp}")
    time.sleep(1)
