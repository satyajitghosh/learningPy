class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        m=len(s1)
        n=len(s2)
        mydict = {}

        def mds(i,j):
            if i>=m:
                return sum([ord(c) for c in s2[j:]])
            if j>=n:
                return sum([ord(c) for c in s1[i:]])
            if (i,j) not in mydict:
                if s1[i]==s2[j]:
                    mydict[(i,j)] = mds(i+1,j+1)
                else:
                    mydict[(i,j)] = min((ord(s2[j]) + mds(i,j+1)),(ord(s1[i]) + mds(i+1,j)))
            return mydict[(i,j)]
        
        return mds(0,0)



        