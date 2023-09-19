'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have 
security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Solution - 
For a given list of nums, there could be two options
- loot the first, not loot the second, find the max of the loot starting with the 3rd.
- spare the first, find the max of the loot starting the 2nd house.
- the max loot for i is the max of the two above choices.
- we start with the array given and index i keeps moving right
- till a point at which t reaches l/l-1, which represent the boundary conditions. 
- the values for max loot are memoised in the dictionary loot.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        loot = {}
        l = len(nums)-1

        def robhouse(i):
            if i in loot:
                return loot[i]
            else:
                if i==l:
                    loot[i] = nums[l]
                elif i==l-1:
                    loot[i] = max(nums[l-1],nums[l])
                else:
                    loot[i] = max(nums[i] + robhouse(i+2),robhouse(i+1))
                return loot[i]
        return robhouse(0)

        