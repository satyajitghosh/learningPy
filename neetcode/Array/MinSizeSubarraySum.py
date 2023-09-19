from typing import List
import numpy as np
import numpy as np
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minlen = float('inf')
        l = r = 0
        s = 0
        
        for r in range(len(nums)):
            s = s + nums[r]
            while s>=target:
                minlen = min((r-l+1),minlen)
                s = s - nums[l]
                l = l + 1
        return 0 if minlen ==float('inf') else minlen

        
            
if __name__ == '__main__':
    sol = Solution()
    ln=sol.minSubArrayLen(target = 4, nums = [1,4,4])
    print(ln)


        