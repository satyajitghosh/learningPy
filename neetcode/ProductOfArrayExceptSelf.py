'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1] * len(nums)
        post = [1] * len(nums)
        result = [1] * len(nums)

        mul = 1
        for i in (range(len(nums))):
            mul = mul * nums[i]
            pre[i] = mul

        revnums = nums.copy()
        revnums.reverse()

        mul=1
        for i in (range(len(revnums))):
            mul = mul * revnums[i]
            post[i] = mul
        
        post.reverse()

        result[0] = post[1]
        for i in (range(1,len(nums)-1)):
            result[i] = pre[i-1] * post[i+1]
        result[len(nums)-1] = pre[len(nums)-2]

        return result