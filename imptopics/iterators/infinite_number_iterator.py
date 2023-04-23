
class InfiniteNumberIterator:
    
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self.num
    
    def __next__(self):
        self.num +=1
        return self.num

class NumberIterator:
    def __init__(self,max:int):
        self.max = max
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self)->int:
        if self.num < self.max:
            self.num += 1
            return self.num
        else:
            raise StopIteration

def main():
    for num in NumberIterator(3):
        print(num)

if __name__=='__main__':
    main()

