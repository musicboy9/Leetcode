"""
Runtime
1883
ms

Beats
61.56%
of users with Python3

Memory
29.00
MB

Beats
53.48%
of users with Python3
"""

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        result = [["." for _ in box] for _ in box[0]]
        for row_index in range(len(box)):
            row = box[row_index]
            new_row = ["." for _ in row]

            temp_rock_count = 0
            for col_index in range(len(row)):
                if row[col_index] == "#":
                    temp_rock_count += 1
                elif row[col_index] == "*":
                    if temp_rock_count > 0:
                        for rock in range(1, temp_rock_count+1):
                            new_row[col_index-rock] = "#"
                    new_row[col_index] = "*"
                    temp_rock_count = 0
            if temp_rock_count > 0:
                for rock in range(1, temp_rock_count+1):
                    new_row[-rock] = "#"
            
            new_col_index = len(box) - 1 - row_index
            for new_row_index in range(len(row)):
                result[new_row_index][new_col_index] = new_row[new_row_index]

        return result