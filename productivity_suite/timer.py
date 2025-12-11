import time

def timer_menu():
    secs = int(input("Enter seconds: "))
    while secs:
        print(f"Time left: {secs}s", end="\r")
        time.sleep(1)
        secs -= 1
    print("\nTime's up!")
