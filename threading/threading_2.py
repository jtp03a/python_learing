import time
from threading import Thread

# Work to be done
def add_data(data):
    database.append(data)
    time.sleep(2)

# Creating the workers, and passing individual arguments to each of them

database = []
threads = []

for i in range(4):
    t = Thread(target=add_data, args=(i,))
    threads.append(t)
    t.start()
    
print(database)
