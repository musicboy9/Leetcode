from collections import defaultdict
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row_range = range(len(mat))
        col_range = range(len(mat[0]))
        def in_range(row, col):
            return row in row_range and col in col_range
        
        dist_dict = {}
        
        last_updated_coord = set()
        last_updated_val = 0

        for row in row_range:
            for col in col_range:
                if mat[row][col] == 0:
                    dist_dict[(row, col)] = 0
                    last_updated_coord.add((row, col))

        while last_updated_coord:
            new_last_updated_coord = set()
            last_updated_val = last_updated_val + 1
            for coord in last_updated_coord:
                row, col = coord
                candidates = [
                    (row-1,col),
                    (row+1,col),
                    (row,col-1),
                    (row,col+1),
                ]
                for cand in candidates:
                    if in_range(*cand) and cand not in dist_dict:
                        dist_dict[cand] = last_updated_val
                        new_last_updated_coord.add(cand)
            last_updated_coord = new_last_updated_coord
        
        result = mat
        for row in row_range:
            for col in col_range:
                result[row][col] = dist_dict[(row, col)]
        return result
        