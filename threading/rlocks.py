import threading, time, random

# Refer to README.md for the problem instructions


class AddThread( threading.Thread ):
    def __init__(self, name, lock):
        super().__init__()
        self.t = threading.Thread(name=name, target=self.run)
        self.lock = lock
    
    def run(self):
        self.lock.acquire()
        r = random.randint(1,3)
        global number
        try:
            number += 1
            time.sleep(r)
            number += 1
        finally:
            self.lock.release()


class MultiplyThread( threading.Thread ):
    def __init__(self, name, lock):
        super().__init__()
        self.t = threading.Thread(name=name, target=self.run)
        self.lock = lock
    
    def run(self):
        self.lock.acquire()
        r = random.randint(1,3)
        global number
        try:
            number *= 2
            time.sleep(r)
            number *= 2
        finally:
            self.lock.release()


if __name__ == "__main__":
    number = 1

    lock = threading.RLock()

    thread1 = AddThread("thread1", lock)
    thread2 = MultiplyThread("thread2", lock)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Number is: {}".format(number))
