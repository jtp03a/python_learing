import threading, time, random, logging

# Refer to README.md for the problem instructions

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

class AddThread( threading.Thread ):
    def __init__(self, name, lock):
        super().__init__()
        self.t = threading.Thread(name=name, target=self.run)
        self.lock = lock
    
    def run(self):
        logging.debug('Waiting for a lock')
        self.lock.acquire()
        r = random.randint(1,3)
        global number
        try:
            logging.debug('Acquired a lock')
            logging.debug('First Increment')
            number += 1
            logging.debug(f'Number is: {number}')
            logging.debug('Sleeping')
            time.sleep(r)
            logging.debug('Second Increment')
            number += 1
            logging.debug(f'Number is {number}')
        finally:
            logging.debug('Releasing lock')
            self.lock.release()


class MultiplyThread( threading.Thread ):
    def __init__(self, name, lock):
        super().__init__()
        self.t = threading.Thread(name=name, target=self.run)
        self.lock = lock
    
    def run(self):
        logging.debug('Waiting for a lock')
        self.lock.acquire()
        r = random.randint(1,3)
        global number
        try:
            logging.debug('Acquired a lock')
            logging.debug('First Multiply')
            number *= 2
            logging.debug(f'Number is {number}')
            logging.debug('Sleeping')
            time.sleep(r)
            logging.debug('Second Multiply')
            number *= 2
            logging.debug(f'Number is {number}')
        finally:
            logging.debug('Releasing lock')
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
