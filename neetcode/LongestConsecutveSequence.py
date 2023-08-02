'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        mydict = collections.defaultdict()
        
        for num in nums:
            mydict[num] = False
        
        maxseqlength = 0
        

        def exists(num):
            return True if num in mydict else False
        
        def leftseqlen(num):
            if not exists(num-1):
                return 0
            else:
                num -=1
                mydict[num] = True
                return (1 + leftseqlen(num))
        
        def rightseqlen(num):
            if not exists(num+1):
                return 0
            else:
                num +=1
                mydict[num] = True
                return (1 + rightseqlen(num))

        for num in nums:
            seqlength = 0
            if not mydict[num]:
                seqlength = leftseqlen(num) + 1 + rightseqlen(num)
                if seqlength > maxseqlength:
                    maxseqlength = seqlength
        
        return maxseqlength


                


            
