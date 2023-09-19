from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        myset = set()
        i=j=0
        maxlen = float('-inf')
        if len(s) <=0:
            return 0
        while j<n:
            if s[j] not in myset:
                myset.add(s[j])
                ln = (j-i) + 1
                if ln > maxlen:
                    maxlen = ln
                j = j+1
            else:
                myset.remove(s[i])
                i = i+1

        return maxlen


if __name__ == '__main__':
    sol = Solution()
    ans = sol.lengthOfLongestSubstring("abcabcbb")
    print(ans)