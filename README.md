# System-Monitor---Python
Basic System Monitor with Logging in Python

# Core Functionality
1. *CPU Usage*: Get and display current CPU usage as percentage
2. *Memory Usage*: Get and display total RAM usage (MB)
3. *Timestamps*: Display a timestamp for each reading

to start off, we'll need to import `time` & `psutil`

```python
import time
import psutil
```
- Importing *time* will grant the use of `time.sleep()`, this is useful to stop the script from running too rapidly and consuming excess resources.
- we could also use `time.strftime()` to record when each reading of CPU and memory usage was taken.
- as for `psutil` library, its a convenient way for Python to get information about running processes.

```python
import time
import psutil

while True:
    cpu = psutil.cpu_percent()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    print(f"CPU Usage: {cpu}% at {timestamp}")
    time.sleep(1)
```

Here is the code to print out the CPU Usage every second along with the timestamp, however, I wish to add a feature that lets the user to quit when the user presses a button, or rather, 
prompt the user to give the number of cpu readings.


```python
import time
import psutil



while True:
    numOfReadings = input("Number of CPU readings?: ")
    
    if numOfReadings.isdigit():
        numOfReadings = int(numOfReadings)
        break
    else:
        print("Invalid Input! Please enter a number")
    

count = 0
while count < numOfReadings:
    cpu = psutil.cpu_percent()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    print(f"CPU Usage: {cpu}% at {timestamp}")
    count += 1
    time.sleep(1)
```

The first *while* loop ensures the user enters a number and not a letter, in case they do, it'll print a message indicating that only numbers are valid and continuously loop until the user enters a number, which is converted to integer, because the built-in function *input* will store the users input as a string datatype.

Now to add *memory usage*
```python
memory_usage = psutil.virtual_memory()
```
and print it along with the cpu and timestamp

*Format it so its readable*:
```python
import time
import psutil



while True:
    numOfReadings = input("Number of CPU readings?: ")
    
    if numOfReadings.isdigit():
        numOfReadings = int(numOfReadings)
        break
    else:
        print("Invalid Input! Please enter a number")
    

count = 0
while count < numOfReadings:
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

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
```
