## Implementing locks

# Just an improved way to apply locks is to use it with contex - ie. with the with statement
# That way we dont forget to release the lock.

from multiprocessing import Process,Value,Lock

def add_num(number:Value,lock:Lock):
   for i in range(10000):
      with lock:
         number.value += 1

def substract_num(number:Value,lock:Lock):
   for i in range(10000):
      with lock:
         number.value -= 1
      
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
