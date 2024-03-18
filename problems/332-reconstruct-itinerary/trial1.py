import copy
from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_count = len(tickets)

        avail_tickets_by_dep = defaultdict(list)
        for index in range(ticket_count):
            dep, des = tickets[index]
            avail_tickets_by_dep[dep].append((des, index))
        def rec(tickets, curr, count, used_ticket_set):
            if count == ticket_count:
                return []
            if not tickets[curr]:
                return False
            options = []
            for des, index in tickets[curr]:
                if index in used_ticket_set:
                    continue
                next_result = rec(tickets, des, count+1, used_ticket_set | set([index]))
                if next_result is False:
                    continue
                elif next_result == []:
                    heapq.heappush(options, [curr, des])
                else:
                    heapq.heappush(options, [curr] + next_result)
            if not options:
                return False
            return heapq.heappop(options)
            
        return rec(avail_tickets_by_dep, "JFK", 0, set([]))