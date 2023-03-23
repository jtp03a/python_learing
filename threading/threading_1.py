import time
from threading import Thread

# Work to be done
def sleeper(i):
    print("thread {:d} sleeps for 5 seconds\n".format(i))
    time.sleep(5)
    print("thread {:d} woke up\n".format(i))

# Creating the workers, and passing individual arguments to each of them
for i in range(10):
    t = Thread(target=sleeper, args=(i,))
    t.start()
