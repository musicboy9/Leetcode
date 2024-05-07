"""
Runtime
234
ms
Beats
40.30%
of users with Python3

Memory
16.90
MB

Beats
66.75%
of users with Python3
"""

from collections import defaultdict
class Solution:
    def subset_from_sorted_nums(self, start_index):
        if start_index in self.processed_map:
            return self.processed_map[start_index]
        
        start_num = self.sorted_nums[start_index]
        result = [start_num]
        for target_index in range(start_index+1, len(self.sorted_nums)):
            if self.sorted_nums[target_index] % start_num == 0:
                temp_result = [start_num] + self.subset_from_sorted_nums(target_index)
                if len(temp_result) > len(result):
                    result = temp_result
        self.processed_map[start_index] = result
        if len(result) > len(self.result):
            self.result = result
        return result

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        self.result = []
        self.sorted_nums = sorted(nums)
        self.processed_map = {}
        for index in range(len(self.sorted_nums)):
            self.subset_from_sorted_nums(index)
        
        return self.result
