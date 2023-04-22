# This example shows the implementation of the two deorators through functions only.
# This showshow the function can be called through the decorators with a less 
# wordy syntax, using the @ symbol

from abc import ABC,abstractmethod
import math
import time
from typing import Callable,Any

def is_prime(number:int)->bool:
    '''Returns True if the number is Prime'''
    if number <= 2:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def benchmark(func:Callable[...,Any]) -> Callable[...,Any]:
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        value = func(*args,**kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {end_time-start_time} seconds.")
        return value
    return wrapper

def log(func:Callable[...,Any])->Callable[...,Any]:
    def wrapper(*args,**kwargs):
        print(f"Starting:{func.__name__}")
        value = func(*args,**kwargs)
        print(f"Completed:{func.__name__}")
    return wrapper

@benchmark
@log
def countprimes(upperlimit:int)->int:
    count = 0
    for i in range(1,upperlimit):
        if is_prime(i):
            count = count + 1
    return count

def main():
    print(countprimes(10000))

if __name__=='__main__':
    main()

