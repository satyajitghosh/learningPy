from multiprocessing import Process,Value,Lock,Array
from multiprocessing import Queue
import time

def square_numbers(num,q,lock):
    for i in num:
        with lock:
            q.put(i*i)
        time.sleep(0.01)

def negate_numbers(num,q,lock):
    for i in num:
        with lock:
            q.put(i*-1)

if __name__=='__main__':
    q = Queue()
    numbers = range(1,5)
    lock = Lock()
    p1 = Process(target=square_numbers,args=(numbers,q,lock))
    p2 = Process(target=negate_numbers,args=(numbers,q,lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    while not q.empty():
        print(q.get())
