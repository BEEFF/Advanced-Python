# TIME LIMITED FUNCTIONS # 

# We want to execute function (a) for no more than 2 seconds
# We want to execute function (b) for no more than 5 seconds

# Solution: Create a class that loops the desired function over a timeout
#           Start both processes using a multiprocessing process

import time
import multiprocessing

def a(*args):
    print('a is running')

def b(*args):
    print("b is running")

class TimeoutProcess:
    def __init__(self, function, timeout, args=[]):
        self.process = multiprocessing.Process(target=self.loop, args=args)
        self.function = function
        self.timeout = timeout

    def start(self):
        self.process.start()

    def loop(self, *args):
        start = time.time()
        while (time.time() - start) < self.timeout:
            self.function(args)
            time.sleep(1)
       

if __name__ == '__main__':

    # Run functions a and b with different timeouts
    p1 = TimeoutProcess(a, 2)
    p2 = TimeoutProcess(b, 5)
    p3 = TimeoutProcess(a, 7)

    # Start a and b
    p1.start()
    p2.start()

    print("Launched a and b")

    # Wait 4 seconds before starting a again
    time.sleep(4)
    p3.start()

    print("Launched a again")


    


    

        

    


