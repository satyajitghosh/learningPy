'''
Solution - https://www.youtube.com/watch?v=cjWnW0hdF1Y

'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        lsub = [1] * n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n,1):
                if (nums[i] < nums[j]):
                    lsub[i] = max(lsub[i],1+lsub[j])
        
        return max(lsub)






        