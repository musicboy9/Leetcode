"""
Runtime
57
ms
Beats
62.72%

Memory
18.86
MB
Beats
18.64%
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = set()
        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.add(num)
        return list(result)
