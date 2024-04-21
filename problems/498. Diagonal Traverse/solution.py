"""
Runtime
138
ms

Beats
92.79%
of users with Python3

Memory
19.65
MB

Beats
63.49%
of users with Python3
"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        height = len(mat)
        width = len(mat[0])
        if height == 1:
            return mat[0]
        if width == 1:
            return [row[0] for row in mat]
        
        RIGHT_UP = 0
        LEFT_DOWN = 1

        diag = RIGHT_UP
        row, col = 0, 0
        result = []
        while True:
            result.append(mat[row][col])
            if row == height-1 and col == width-1:
                break
            if diag == RIGHT_UP:
                if row == 0:
                    diag = LEFT_DOWN
                    if col == width-1:
                        row += 1
                    else:
                        col += 1
                elif col == width-1:
                    diag = LEFT_DOWN
                    row += 1
                else:
                    row -= 1
                    col += 1
                continue
            if diag == LEFT_DOWN:
                if col == 0:
                    diag = RIGHT_UP
                    if row == height-1:
                        col += 1
                    else:
                        row += 1
                elif row == height-1:
                    diag = RIGHT_UP
                    col += 1
                else:
                    col -=1
                    row += 1
                continue
        return result
                    
        