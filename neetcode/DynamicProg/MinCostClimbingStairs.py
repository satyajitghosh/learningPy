'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Solution - 
So, to clarify the question - you can start at index 0 or 1,
and you can either take one or two steps from where you are,
and you must reach the end of the staircase - which is the last cell of the list + 1.
If we are on the last step and the second last step,
we can directly reach the end from here without any additional cost.
So, we can calulate the cost from the thrid step from the end and work our way down.
On a given step i, the choices are to go to 
i+1 - then we have to pay the cost of being in i+1 and the total cost from i+1
i+2 - then we have to pay the cost of being in i+2 and the total cost from i+2
Therefore, when at i, we will choose the path which costs less.
totalCost[i] = min((totalCost[i+1]+cost[i+1]),(totalCost[i+2]+cost[i+2])) 
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        totalCost = [0] * len(cost)
        
        i = len(cost) -1 -2 # this is the index of 3rd element from the end
        
        while i>=0:

            totalCost[i] = min((totalCost[i+1]+cost[i+1]),(totalCost[i+2]+cost[i+2]))
            i-=1
        
        return(min(totalCost[0]+cost[0],totalCost[1]+cost[1]))

