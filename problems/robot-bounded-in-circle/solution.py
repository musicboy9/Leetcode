"""
Runtime
33
ms

Beats
71.98%
of users with Python3

Memory
16.44
MB

Beats
90.36%
of users with Python3
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        L_CHANGE = {
            "N": "W",
            "W": "S",
            "S": "E",
            "E": "N"
        }
        R_CHANGE = {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N"
        }
        def go(status, x, y):
            if status == "N":
                return x, y+1
            if status == "W":
                return x-1, y
            if status == "E":
                return x+1, y
            if status == "S":
                return x, y-1
                

        status = "N"
        x = 0
        y = 0
        
        four_instructions = (instructions * 4)
        for instruction in four_instructions:
            if instruction == "G":
                x, y = go(status, x, y)
            elif instruction == "L":
                status = L_CHANGE[status]
            else:
                status = R_CHANGE[status]
        
        return x==0 and y==0