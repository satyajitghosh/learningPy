'''
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        numset = set()
        for num in nums:
            if num in numset:
                return True
            else:
                numset.add(num)
        return False