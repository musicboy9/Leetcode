"""
Runtime
93
ms
Beats
42.22%
of users with Python3

Memory
41.01
MB
Beats
5.10%
of users with Python3
"""
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        line_points = defaultdict(set)
        for index_1 in range(len(points)-1):
            for index_2 in range(index_1+1, len(points)):
                x_1, y_1 = points[index_1]
                x_2, y_2 = points[index_2]
                # ax + by + c = 0
                if x_1 == x_2:
                    a = 1
                    b = 0
                    c = -x_1
                elif y_1 == y_2:
                    a = 0
                    b = 1
                    c = -y_1
                else:
                    b = 1
                    a = (y_2-y_1)/(x_1-x_2)
                    c = -a*x_1 - b*y_1
                
                line_points[(a,b,c)].update([(x_1,y_1), (x_2,y_2)])
        result = 0
        for _, val in line_points.items():
            result = max(result, len(val))
        return result

        