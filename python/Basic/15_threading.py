import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffer():
    time.sleep(4)
    print("You drink coffer")


def study():
    time.sleep(5)
    print("You study")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffer, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

# eat_breakfast()
# drink_coffer()
# study()


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
