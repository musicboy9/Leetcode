"""
Runtime
36
ms

Beats
84.05%
of users with Python3

Memory
16.50
MB

Beats
76.13%
of users with Python3
"""

from collections import defaultdict
from functools import cmp_to_key

def str_cmp(a, b):
    if a+b < b+a:
        return 1
    else:
        return -1

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        starting_digit_nums = defaultdict(list)
        for num in nums:
            starting_digit = int(str(num)[0])
            starting_digit_nums[starting_digit].append(str(num))
        
        result = ""
        for digit in range(9, -1, -1):
            sorted_list = sorted(starting_digit_nums[digit], key=cmp_to_key(str_cmp))
            for str_num in sorted_list:
                result += str_num
        
        if result[0] == "0":
            return "0"
        return result
        
        
        