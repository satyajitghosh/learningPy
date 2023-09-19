'''
Tribonacci - Same as fibonacci.
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        mydict = {}
        mydict[0] = 0
        mydict[1] = 1
        mydict[2] = 1
    
        def tribo(n):
            if n in mydict:
                return mydict[n]
            else:
                mydict[n] = (tribo(n-1) + tribo(n-2) + tribo(n-3))
                return mydict[n]
        
        return tribo(n)