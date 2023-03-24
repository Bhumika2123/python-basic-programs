import threading
import time

def timer():
    print()
    print()
    count= 0
    while True:
        time.sleep(3)
        count+=1
        print("login time",count)

x= threading.Thread(target=timer, daemon=True)
x.start()

answer = input("enter")