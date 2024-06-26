"""
Runtime: 723 ms, faster than 26.46% of Python3 online submissions for Detonate the Maximum Bombs.
Memory Usage: 20.4 MB, less than 5.99% of Python3 online submissions for Detonate the Maximum Bombs.
"""

from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bombs_in_range = defaultdict(set)
        for i in range(len(bombs)):
            for j in range(i, len(bombs)):
                dist = ((bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2)**0.5
                if dist <= bombs[i][2]:
                    bombs_in_range[i].add(j)
                if dist <= bombs[j][2]:
                    bombs_in_range[j].add(i)
        
        def get_target_bombs(i, visited):
            result = bombs_in_range[i].copy()
            for j in bombs_in_range[i]:
                if not visited[j]:
                    visited[j] = True
                    result |= get_target_bombs(j, visited)
            return result
        
        result = 0
        for i in range(len(bombs)):
            visited = [False for _ in bombs]
            result = max(
                result,
                len(get_target_bombs(i, visited))
            )
        return result
                
            
        
