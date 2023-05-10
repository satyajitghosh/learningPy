## Implementing locks

from multiprocessing import Process,Value,Lock

def add_num(number:Value,lock:Lock):
   for i in range(10000):
      lock.acquire()
      number.value += 1
      lock.release()

def substract_num(number:Value,lock:Lock):
   for i in range(10000):
      lock.acquire()
      number.value -= 1
      lock.release()

if __name__=='__main__':
    # i in the first argument says that the expect data type is integer.
    # and the initial value is 0
    shared_number = Value('i',0)
    lock = Lock()
    p1 = Process(target=add_num,args=(shared_number,lock))
    p2 = Process(target=substract_num,args=(shared_number,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'Final Value = {shared_number.value}')

# Now, with lock, we see that the final value is 0.
