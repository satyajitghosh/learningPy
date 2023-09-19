'''
Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated sequence 
of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple 
times in the segmentation.

Solution - Note that DP is applied with the following logic.
we traverse the string one palce at a time. If the left part is
present in worddict and the right part is True, then the 
combination is True.
IF after traversing the string, we dont find a combination
where the left substring is part of the dict and the right subpart is true
then the string is false.
mdict[m] = True
This is done because it is a boundary condition.
When p = m+1
then the string is fully represnted in the left subpart and the left subpart
is part of the worddict, then the right part need not be checked
as it is of length 0.
If the right part need not be checked, then in other words, it
can be assumed to be true with out any adverse consequances.
''' 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        mydict={}
        m= len(s)
        mydict[m] = True

        def wb(i):
            if i in mydict:
                return mydict[i]
            else:
                for p in range(i,m):
                    if s[i:p+1] in wordDict:
                        if wb(p+1):
                            mydict[i] = True
                            return mydict[i]
                mydict[i] = False
                return False
        
        return wb(0)
