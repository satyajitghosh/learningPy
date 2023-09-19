'''
Solution - 
https://www.youtube.com/watch?v=xsyteDgyqXk
'''
class Solution:

    def isPalin(self,l,r,s):
        m = len(s)
        while l>0 and r<(m-1) and s[l-1]==s[r+1]:
            l-=1
            r+=1
        return l,r,(r-l+1)

    def longestPalindrome(self, s: str) -> str:

        l=r=0
        maxLen=0

        for i in range(len(s)-1):

            # check the largest odd length palindrome with i at the centre
            templ,tempr,templen = self.isPalin(i,i,s)
            if templen > maxLen:
                l,r,maxLen = templ,tempr,templen

            # check the largest even length palindrome with i,i+1 at the centre.
            if s[i] == s[i+1]:
                templ,tempr,templen = self.isPalin(i,i+1,s)
                if templen > maxLen:
                    l,r,maxLen = templ,tempr,templen
        
        return(s[l:r+1])