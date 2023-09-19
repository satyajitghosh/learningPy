'''
Given an n x n array of integers matrix, return the minimum sum of 
any falling path through matrix.
A falling path starts at any element in the first row and chooses 
the element in the next row that is either directly below or diagonally 
left/right. Specifically, the next element from position (row, col) will 
be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
'''
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        mydict = {}

        def minsum(i,j):
            if (i,j) in mydict:
                return mydict[(i,j)]
            else:
                ls = []
                ls.append(minsum(i+1,j-1) if ((i+1)<=(m-1) and (j-1)>=0) else None)
                ls.append(minsum(i+1,j) if ((i+1)<=(m-1)) else None)
                ls.append(minsum(i+1,j+1) if ((i+1)<=(m-1) and (j+1)<=(m-1)) else None)
                ls = list(filter(lambda x: x is not None,ls))
                mydict[(i,j)] = (matrix[i][j] + min(ls)) if ls else matrix[i][j]
                return mydict[(i,j)]
        j = 0
        result = minsum(0,0)
        while j<m:
            mydict[(0,j)] = minsum(0,j)
            result = mydict[(0,j)] if mydict[(0,j)] < result else result
            j+=1
        
        return result