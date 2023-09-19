'''
There is a robot on an m x n grid. The robot is initially located at the 
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right 
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right 
at any point in time.
Given the two integers m and n, return the number of possible unique paths that 
the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.
Start from 0,0. Go to m-1,n-1.
from m-2,n-1 and from m-1,n-2 there are only one paths available to the end respectively.
from the rest of the cells i,j, we can go to i+1,j or i,j+1, provided the destination cells
lie within the boundary.
and therefore the number of paths from i,j = sum of paths from the two above destinations.

'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mydict ={}
        mydict[(m-1,n-1)] = 1
        mydict[(m-2,n-1)] = 1
        mydict[(m-1,n-2)] = 1

        def numpaths(i,j):
            if (i,j) in mydict:
                return mydict[(i,j)]
            else:
                mydict[(i,j)] = (numpaths(i+1,j) if (i+1)<=(m-1) else 0) + (numpaths(i,j+1) if (j+1)<=(n-1) else 0) 
                return(mydict[(i,j)])
        
        return(numpaths(0,0))
        