import time
from threading import Thread

# Work to be done
def add_data(data):
    database.append(data)
    time.sleep(2)

# Creating the workers, and passing individual arguments to each of them

database = []
threads = []


t1 = Thread(target=add_data, args=(1,))
threads.append(t1)
t1.start()

t2 = Thread(target=add_data, args=(2,))
threads.append(t2)
t2.start()

t3 = Thread(target=add_data, args=(2,))
threads.append(t3)
t3.start()

t4 = Thread(target=add_data, args=(3,))
threads.append(t4)
t4.start()
    
print(database)
