class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        grid = set()
        for row in range(rows):
            for col in range(cols):
                grid.add((row, col))
        
        def add_coord(r, c):
            if (r, c) in grid:
                result.append([r, c])

        total_num = rows * cols
        radius = 1
        result = [[rStart, cStart]]
        current_row = rStart
        current_column = cStart
        while len(result) < total_num:
            for _ in range(radius):
                current_column += 1
                add_coord(current_row, current_column)
            for _ in range(radius):
                current_row += 1
                add_coord(current_row, current_column)
            radius += 1
            for _ in range(radius):
                current_column -= 1
                add_coord(current_row, current_column)
            for _ in range(radius):
                current_row -= 1
                add_coord(current_row, current_column)
            radius += 1
        return result
