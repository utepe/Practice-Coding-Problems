'''
Implement a job scheduler which takes in a function f
and an integer n, and calls f after n milliseconds.
'''
import time
def hello():
    print("Hello World")

def scheduler(f, n):
    time.sleep(n/1000)
    f()
    
scheduler(hello, 10000)