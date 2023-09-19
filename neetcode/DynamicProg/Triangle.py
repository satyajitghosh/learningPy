'''
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, you may move to 
either index i or index i + 1 on the next row.
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        m = len(triangle)
        mydict = {}

        def minSum(i,j):
            if (i,j) in mydict:
                return mydict[(i,j)]
            else:
                ls = []
                
                # minsum for i,j will be equal to the sum of the cost of the current cell i,j
                # and the min cost from the next row to the last row. 
                # boundary condition on i should be checked.
                # and the diagonal condition on j should be checked.
                # as for the shape to be a triangle
                # each rows last element would lie in the leading diagonal
                # of the double dimensional array.
                
                if (i+1)<=(m-1):
                    ls.append(minSum(i+1,j))
                if ((i+1)<=(m-1) and (j+1)<=(i+1)):
                    ls.append(minSum(i+1,j+1))
                
                mydict[(i,j)] = triangle[i][j] + (min(ls) if ls else 0)
                return mydict[(i,j)]
        
        return minSum(0,0)
