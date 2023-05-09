import multiprocessing as mp
import math
import time

result1 = []
result2 = []
result3 = []

def calc1(numbers:list):
    for num in numbers:
        result1.append(math.sqrt(num**3))
         
def calc2(numbers:list):
    for num in numbers:
        result2.append(math.sqrt(num**4))

def calc3(numbers:list):
    for num in numbers:
        result3.append(math.sqrt(num**5))

if __name__=='__main__':
    num = list(range(1000000))
    start_time = time.time()
    calc1(num)
    calc2(num)
    calc3(num)
    end_time = time.time()
    elapsed = end_time-start_time
    print(elapsed)

    start_time = time.time()
    p1=mp.Process(target=calc1,args=(num,))
    p2=mp.Process(target=calc1,args=(num,))
    p3=mp.Process(target=calc1,args=(num,))
    p1.start()
    p2.start()
    p3.start()
    end_time = time.time()
    elapsed = end_time-start_time
    print(elapsed)
