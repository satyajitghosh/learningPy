## Implementing locks

# Just an improved way to apply locks is to use it with contex - ie. with the with statement
# That way we dont forget to release the lock.

from multiprocessing import Process,Value,Lock,Array

def add_num(numbers:Array,lock:Lock):
   for i in range(100):
      for i in range(len(numbers)):
         with lock:
            numbers[i] += 1
      
if __name__=='__main__':
    # i in the first argument says that the expect data type is integer.
    # and the initial value is 0
    shared_array = Array('d',[0,100,200])
    print(f'Initial Value = {shared_array[:]}')

    lock = Lock()
    p1 = Process(target=add_num,args=(shared_array,lock))
    p2 = Process(target=add_num,args=(shared_array,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'Final Value = {shared_array[:]}')

# Now, with lock, we see that the final value is 0.
