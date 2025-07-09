
#!/usr/bin/env python3
from time import sleep
sleep_time = input("please enter the amount of time to sleep [s] (default: 0.0001): ")
sleep_time = float(sleep_time) if sleep_time else 0.0001
while True:
    for i in range(0,256):
        print(f"\033[38;2;{255-i};0;0mO\033[00m",end="",flush=True) 
        sleep(sleep_time)
        
    for i in range(0,256):
        print(f"\033[38;2;0;{i};0mO\033[00m",end="",flush=True)
        sleep(sleep_time)

    for i in range(0,256):
        print(f"\033[38;2;{i};255;{i}mO\033[00m",end="",flush=True)
        sleep(sleep_time)

    for i in range(0,256):
        print(f"\033[38;2;{255-i};{255-i};255mO\033[00m",end="",flush=True)
        sleep(sleep_time)

    for i in range(0,256):
        print(f"\033[38;2;0;0;{255-i}mO\033[00m",end="",flush=True)
        sleep(sleep_time) 

    for i in range(0,256):
        print(f"\033[38;2;{i};{i};0mO\033[00m",end="",flush=True)
        sleep(sleep_time)

    for i in range(0,256):
        print(f"\033[38;2;255;255;{i}mO\033[00m",end="",flush=True)
        sleep(sleep_time)

    for i in range(0,256):
        print(f"\033[38;2;255;{255-i};{255-i}mO\033[00m",end="",flush=True)
        sleep(sleep_time)
        
   
