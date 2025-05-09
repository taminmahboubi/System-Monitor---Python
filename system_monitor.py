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
    
