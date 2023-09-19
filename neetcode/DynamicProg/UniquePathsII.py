'''
You are given an m x n integer array grid. There is a robot initially located at the 
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner 
(i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot 
takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right 
corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        mydict={}
        #This is because 1 denotes an obstacle and numpaths should be equal to 0 if there
        #is an obstacle at the cell. 0 indicates free space.
        mydict[(m-1,n-1)] = 1 if obstacleGrid[m-1][n-1]==0 else 0

        def numpaths(i,j):
            if (i,j) in mydict:
                return mydict[(i,j)]
            else:
                # checking both boundary conditions and the free space.
                # ie. the next cell down/right should be within the boundary and free
                # Only then can it be a part of the possible paths from i,j.     
                down  = numpaths(i+1,j) if ((i+1)<=(m-1) and obstacleGrid[i+1][j]==0) else 0
                right = numpaths(i,j+1) if ((j+1)<=(n-1) and obstacleGrid[i][j+1]==0) else 0
                mydict[(i,j)] = down + right
                return mydict[(i,j)]
        
        if obstacleGrid[0][0] == 0:
            return numpaths(0,0)
        else:
            return 0