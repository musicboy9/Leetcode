"""
Runtime
295
ms
Beats
11.39%
of users with Python3

Memory
17.85
MB

Beats
60.01%
of users with Python3
"""

class Solution:
    def find_target_rec(self, nums, target):
        dict_key = (nums, target)
        if dict_key in self.nums_and_target_to_ways:
            return self.nums_and_target_to_ways[dict_key]

        if len(nums) == 0:
            if target == 0:
                return 1
            else:
                return 0
        
        else:
            self.nums_and_target_to_ways[dict_key] = (
                self.find_target_rec(nums[1:], target + nums[0]) +
                self.find_target_rec(nums[1:], target - nums[0])
            )
            return self.nums_and_target_to_ways[dict_key]
        

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums_and_target_to_ways = {}
        return self.find_target_rec(tuple(nums), target)
        