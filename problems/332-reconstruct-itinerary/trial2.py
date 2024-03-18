import copy
from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_count = len(tickets)

        avail_tickets_by_dep = defaultdict(list)
        for dep, des in tickets:
            avail_tickets_by_dep[dep].append(des)
        def rec(tickets, curr, count):
            if count == ticket_count:
                return []
            if not tickets[curr]:
                return False
            options = []
            for des in tickets[curr]:
                new = copy.deepcopy(tickets)
                new[curr].remove(des)
                next_result = rec(new, des, count+1)
                if next_result is False:
                    continue
                elif next_result == []:
                    heapq.heappush(options, [curr, des])
                else:
                    heapq.heappush(options, [curr] + next_result)
            if not options:
                return False
            return heapq.heappop(options)
            
        return rec(avail_tickets_by_dep, "JFK", 0)