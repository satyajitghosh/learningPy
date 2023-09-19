class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dt = [[0]*(n+1) for _ in range(m+1)]

        for i in reversed(range(m+1)):
            dt[i][n] = m-i

        for j in reversed(range(n+1)):
            dt[m][j] = n-j
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if word2[i]==word1[j]:
                    dt[i][j] = dt[i+1][j+1]
                else:
                    dt[i][j] = 1 + min(dt[i+1][j+1],dt[i][j+1],dt[i+1][j])
        
        return dt[0][0]
