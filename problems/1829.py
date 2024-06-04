"""
Runtime
670
ms

Beats
63.42%
of users with Python3

Memory
34.07
MB

Beats
77.27%
of users with Python3
"""

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_val = 2**maximumBit
        temp = nums[0]
        temp_answer = [temp]
        for num in nums[1:]:
            temp = temp ^ num
            temp_answer.append(temp)
        return [(~temp + max_val) for temp in temp_answer][::-1]
