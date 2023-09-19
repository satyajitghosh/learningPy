from typing import List
from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=len(nums)-1
        i=0

        while i <= r:
            if nums[i]==0:
                temp = nums[i]
                nums[i] = nums[l]
                nums[l] = temp
                i = i+1
                l = l+1
            elif nums[i]==2:
                temp = nums[i]
                nums[i] = nums[r]
                nums[r] = temp
                if nums[i] !=0:
                    i = i+1
                r = r-1
            else:
                i = i+1
    
sol = Solution()
ls = [2,0,2,1,1,0]
sol.sortColors(ls)
print(ls)