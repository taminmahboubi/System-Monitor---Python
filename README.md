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


