"""
Runtime
945
ms

Beats
89.15%
of users with Python3

Memory
25.61
MB

Beats
95.35%
of users with Python3
"""
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        result = 0
        for i in range(n-1, 1, -2):
            result += abs(cost[i-1] - cost[i])
            cost[(i//2)-1] += max(cost[i-1], cost[i])
        return result
