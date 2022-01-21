# TIME LIMITED FUNCTION # 
# We want a function to run for no more than 2 seconds. 
# This can be done using the multiprocessing module

import time
import multiprocessing

MAX_WAIT_TIME = 2

def never_ending_function(name):
    """ A never ending function that outputs execution time """
    start_time = time.time()
    while True:
        print('\r' + "{0} been running for: {1} seconds...".format(name, round(time.time() - start_time)), end="")

if __name__ == '__main__':
    # Create a never ending function process
    process = multiprocessing.Process(target=never_ending_function, args=('I'))
    process.start()

    # Wait for MAX_WAIT_TIME until OR until the process finishes
    process.join(MAX_WAIT_TIME)

    if process.is_alive():
        process.terminate()