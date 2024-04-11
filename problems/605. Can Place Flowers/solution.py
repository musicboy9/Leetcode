"""
Runtime
125
ms

Beats
87.60%
of users with Python3

Memory
17.83
MB
Beats
12.47%
of users with Python3
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        avail_new_flower_count = 0
        unavail_flower_place = set()
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                unavail_flower_place.update([i-1, i, i+1])
        
        for i in range(len(flowerbed)):
            if i in unavail_flower_place:
                continue
            else:
                avail_new_flower_count += 1
                unavail_flower_place.update([i+1])
        
        return n <= avail_new_flower_count