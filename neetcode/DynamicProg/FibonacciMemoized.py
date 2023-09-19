'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
Memoized fibonacci.
'''
class Solution:
    def fib(self, n: int) -> int:
        mydict = {}
        mydict[0] = 0
        mydict[1] = 1

        def fibo(n):
            if n in mydict:
                return mydict[n]
            else:
                mydict[n] = fibo(n-1) + fibo(n-2)
                return mydict[n]
        
        return fibo(n)