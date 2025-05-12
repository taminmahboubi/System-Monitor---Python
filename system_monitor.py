import time
import psutil
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Access the log file name from the [General] section 
log_file_name = config['General']['log_file_name']

# Access the monitoring interval from the [General] section and convert it to an integer
monitoring_interval = int(config['General']['monitoring_interval'])


while True:
    numOfReadings = input("Number of CPU readings?: ")
    
    if numOfReadings.isdigit():
        numOfReadings = int(numOfReadings)
        log_file = open("system_monitor.log", "a")
        log_file.write("\n")
        break
    else:
        print("Invalid Input! Please enter a number")
    

count = 0
while count < numOfReadings:
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    log_file.write(f"CPU Usage: {cpu_usage}%, Memory Total: {memory_usage.total}, Memory Used: {memory_usage.used}, Timestamp: {timestamp}\n")

    print(f"CPU Usage: {cpu_usage}%  {timestamp}\n")
    print("Memory Usage:")
    print(f"  Total:     {memory_usage.total}")
    print(f"  Available: {memory_usage.available}")
    print(f"  Percent:   {memory_usage.percent}%")
    print(f"  Used:      {memory_usage.used}")
    print(f"  Free:      {memory_usage.free}")
    print(f"  Active:    {memory_usage.active}")
    print(f"  Inactive:  {memory_usage.inactive}")
    print(f"  Buffers:   {memory_usage.buffers}")
    print(f"  Cached:    {memory_usage.cached}")
    print(f"  Shared:    {memory_usage.shared}")
    print(f"  Slab:      {memory_usage.slab}")
    print(f"\nat {timestamp}")
    print("------------------------------")

    count += 1
    time.sleep(1)
    
log_file.close()
    
