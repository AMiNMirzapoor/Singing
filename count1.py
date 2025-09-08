import time
import sys

n = int(input("Enter a number: "))

# 1 second delay at the beginning
time.sleep(1)

def beep():
    sys.stdout.write("\a")
    sys.stdout.flush()

# Growing cycles from 3 to n
for k in range(3, n + 1):
    for i in range(1, k + 1):
        print(f"\033[92m{i}\033[0m", end=" ", flush=True)
        beep()
        time.sleep(1)
    print()
    for i in range(k, 0, -1):
        print(f"\033[93m{i}\033[0m", end=" ", flush=True)
        beep()
        time.sleep(1)
    print()

# Shrinking cycles from n-1 down to 3
for k in range(n - 1, 2, -1):
    for i in range(1, k + 1):
        print(f"\033[92m{i}\033[0m", end=" ", flush=True)
        beep()
        time.sleep(1)
    print()
    for i in range(k, 0, -1):
        print(f"\033[93m{i}\033[0m", end=" ", flush=True)
        beep()
        time.sleep(1)
    print()
