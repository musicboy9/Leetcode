class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        digit_count = len(grid[0])
        for row in grid:
            if row[0] == 0:
                for i in range(digit_count):
                    row[i] = 1 - row[i]
        result = row_count * 2**(digit_count-1)
        for col in range(1, digit_count):
            zero_count = 0
            for row in grid:
                if row[col] == 0:
                    zero_count += 1
            result += (2**(digit_count - col - 1)) * max(zero_count, row_count - zero_count)
        return result
