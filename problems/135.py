"""
Runtime
129
ms
Beats
35.84%
of users with Python3

Memory
19.31
MB

Beats
56.62%
of users with Python3
"""

INCREASING = 1
EQUAL = 0
DECREASING = -1

class Solution:
    def get_status(self, prev_rating, curr_rating):
        if prev_rating > curr_rating:
            return DECREASING
        elif prev_rating == curr_rating:
            return EQUAL
        else:
            return INCREASING

    def append_minimum_candies(self, rate_index):
        if self.status == EQUAL:
            return
        elif self.status == INCREASING:
            for i in range(self.temp_sequence_start_index, rate_index):
                self.candies[i] = max(
                    self.candies[i],
                    i - self.temp_sequence_start_index + 1
                )
        else:
            for i in range(self.temp_sequence_start_index, rate_index):
                self.candies[i] = max(
                    self.candies[i],
                    rate_index - i
                )

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1: return 1

        self.candies = [1 for _ in range(n)]
        self.status = self.get_status(ratings[0], ratings[1])
        self.temp_sequence_start_index = 0
        for rate_index in range(2, n):
            curr_rate = ratings[rate_index]
            new_status = self.get_status(ratings[rate_index-1], curr_rate)
            if self.status == new_status:
                continue
            self.append_minimum_candies(rate_index)
            self.status = new_status
            self.temp_sequence_start_index = rate_index - 1
        self.append_minimum_candies(n)
            
        return sum(self.candies)
