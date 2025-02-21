#15.1
import random as r
import multiprocessing
import datetime as dt
import time
import os

# funcition that prints a processes id and displays a response from the process through the attribute 'data'
def proc(data):
    print("Process %s output: %s!" % (os.getpid(),data,))
          

if __name__ == "__main__":
    # loop 3 times
    for i in range(3):
        # sleep for a random amount of time between 0 and 1
        time.sleep(r.random())
        # get the current time 
        now = dt.datetime.now().time()
        # define process that runs the proc function and inputs a string concatinated with the current time as its argument
        p = multiprocessing.Process(target=proc,
          args=("The current time is: %s" % now,))
        # start the process
        p.start()