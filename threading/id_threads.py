# Identifying Threads

import threading
import time

def f1():
    print( threading.current_thread().name, 'Starting')
    time.sleep(1)
    print( threading.current_thread().name, 'Exiting')

def f2():
    print( threading.current_thread().name, 'Starting')
    time.sleep(2)
    print( threading.current_thread().name, 'Exiting')

def f3():
    print( threading.current_thread().name, 'Starting')
    time.sleep(3)
    print( threading.current_thread().name, 'Exiting')

t1 = threading.Thread(target=f1) # use default name
t2 = threading.Thread(name='f2', target=f2)
t3 = threading.Thread(name='f3', target=f3)

t1.start()
t2.start()
t3.start()

# output

# Thread-1 (f1) Starting
# f2 Starting
# f3 Starting
# Thread-1 (f1) Exiting
# f2 Exiting
# f3 Exiting
