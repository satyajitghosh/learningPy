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

class AbstractComponent(ABC):
    def execute(self,number:int)->int:
        pass
class Corecomponent(AbstractComponent):
    def execute(self,upperlimit:int)->int:
        count = 0
        for i in range(1,upperlimit):
            if is_prime(i):
                count = count + 1
        return count

class AbstractDecorator(AbstractComponent):
    def __init__(self,component:AbstractComponent):
        self._component = component

class BenchmarkDecorator(AbstractDecorator):
    def execute(self,upper_bound:int):
        start_time = time.perf_counter()
        value = self._component.execute(upper_bound)
        end_time = time.perf_counter()
        print(f"{self._component.__class__.__name__} took {end_time-start_time} seconds.")
        return value

def main():
    component = Corecomponent()
    decorator = BenchmarkDecorator(component)
    decorator.execute(10000)

if __name__=='__main__':
    main()

