'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m=len(grid)
        n=len(grid[0])
        
        mydict={}
        mydict[(m-1,n-1)] = grid[m-1][n-1]
         
        def minsum(i,j):
            if (i,j) in mydict:
                return mydict[(i,j)]
            else:
                ls = []
                if (i+1)<=(m-1):
                    ls.append(minsum(i+1,j))
                if (j+1)<=(n-1):
                    ls.append(minsum(i,j+1))
                mydict[(i,j)] = grid[i][j] + min(ls)
                return mydict[(i,j)]
        
        return minsum(0,0)
