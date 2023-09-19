'''
Solution - the primary idea is that the lcs of s and reversed s gives the longest palindromic
subsequence. Ths needs to be though and reviewed.
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        def longestCommonSubsequence(s1,s2):
            m = len(s1)
            n = len(s2)
            dt = [[0]*(n+1) for _ in range(m+1)]

            for row in range(m):
                for col in range(n):
                    if s1[row]==s2[col]:
                        dt[row+1][col+1] = dt[row][col] + 1
                    else:
                        dt[row+1][col+1] = max(dt[row][col+1],dt[row+1][col])
            
            return dt[m][n]
        
        revs=''
        for i in reversed(range(len(s))):
            revs = revs+s[i] 
        
        return longestCommonSubsequence(s,revs)





        