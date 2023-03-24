import threading 
import time




def eat():
    time.sleep(3)
    print("eating")
def study():
    time.sleep(5)
    print("studying")

# creating thread                  it takes less time 3+2=5 sec         1 2 3(execute 1 func) 4 5(execute 2 func)
x= threading.Thread(target=eat)
x.start()
y= threading.Thread(target=study)
y.start()

x.join()         #  join function will do that=> main function will wait for these function to execute after then main will execute in simple these func will join main thread
y.join()
# # without creating thread                it takes more time 3+5=8 sec
# eat()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
