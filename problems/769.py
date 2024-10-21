"""
Runtime
21
ms
Beats
96.40%

Analyze Complexity

Memory
16.42
MB
Beats
71.00%
"""
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunk_num = 0
        target = 0
        for i, val in enumerate(arr):
            target += (val - i)
            if target == 0:
                chunk_num += 1
        return chunk_num
        
