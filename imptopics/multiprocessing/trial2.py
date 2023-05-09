import multiprocessing as mp
import math

def calc(id:int):
    for num in range(10):
        print(f"Process ID : {id}. Result :{round(math.sqrt(num**7))}")

if __name__=='__main__':
    ids = range(10)
    pool = mp.Pool(3)
    pool.map(calc,ids)
