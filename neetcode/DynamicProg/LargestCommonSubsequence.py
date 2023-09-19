'''
Look for explanation here
https://www.youtube.com/watch?v=0yvOxPwe3Dg&list=PLUcsbZa0qzu1oHa_o1-U-ZMR_DgzWvFql&index=3
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1 = len(text1)
        t2 = len(text2)
        q = text1 if t1 >= t2 else text2
        p = text2 if t1 >= t2 else text1

        dt = [[0]*len(q) for _ in range(len(p))]
        dt[0][0] = 1 if q[0]==p[0] else 0
        
        for row in range(len(p)):
            for col in range(len(q)):
                match = (1 if q[col]==p[row] else 0)
                if row==0 and col==0:
                    dt[row][col] = match
                elif row==0:
                    dt[row][col] = max(dt[row][col-1],match)
                elif col==0:
                    dt[row][col] = max(dt[row-1][col],match)
                else:
                    if q[col]==p[row]:
                        dt[row][col] = dt[row-1][col-1]+1
                    else:
                        dt[row][col] = max(dt[row][col-1],dt[row-1][col])
        
        return(dt[(len(p)-1)][(len(q)-1)])
