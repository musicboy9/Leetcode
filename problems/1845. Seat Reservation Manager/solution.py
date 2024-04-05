"""

Runtime
392
ms
Beats
34.37%
of users with Python3

Memory
43.68
MB

Beats
55.15%
of users with Python3
"""

import heapq
class SeatManager:

    def __init__(self, n: int):
        self.avail_seats = list(range(1, n+1))
        

    def reserve(self) -> int:
        min_seat = heapq.heappop(self.avail_seats)
        return min_seat
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.avail_seats, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)