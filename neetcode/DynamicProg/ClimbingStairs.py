'''
Question - 
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Solution - For a given step f(7), at the the 7th step, you can only make
one of two choices take a single step to step 6 or take a double step to step 5.
In case you take a step to step 6, the number of possible paths is f(6)
In case you take a double step to step 5, the number of possible paths is f(5)
Therefore, the number of possible steps from step 7 is f(6) + f(5).
or, f(7) = f(6) + f(5).

Also, the function will calculate same values repeatedly.
the calculations need to be memoized by storing already calculated values
into a dictionary.
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        
        mydict = {}
        mydict[1] = 1
        mydict[2] = 2

        def climb(n):
            if n in mydict:
                return mydict[n]
            else:
                mydict[n] = climb(n-1) + climb(n-2)
                return mydict[n]

        return(climb(n))