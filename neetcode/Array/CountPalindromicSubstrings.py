class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        palcount = 0
        for i in range(n):
            l=r=i
            while l>=0 and r<=(n-1) and s[l]==s[r]:
                palcount += 1
                l-=1
                r+=1
            l = i
            r = i+1
            while l>=0 and r<=(n-1) and s[l]==s[r]:
                palcount += 1
                l-=1
                r+=1
        return palcount
sol = Solution()
ln = sol.countSubstrings('abc')
print(ln)
