from multiprocessing import Process,Value,Array

def add_num(number:Value):
   for i in range(10000):
      number.value += 1

def substract_num(number:Value):
   for i in range(10000):
      number.value -= 1

if __name__=='__main__':
    # i in the first argument says that the expect data type is integer.
    # and the initial value is 0
    shared_number = Value('i',0)
    p1 = Process(target=add_num,args=(shared_number,))
    p2 = Process(target=substract_num,args=(shared_number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'Final Value = {shared_number.value}')
## We expect the final value to be 0 because we are adding 1 10000 
## times ans substracting 1 the same number of times, but that does not happen
## due to something called race condition, which we resolve in the next file.
## using something called Locks.    