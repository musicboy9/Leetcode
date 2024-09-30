from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        group_candidates = defaultdict(set)
        for i, group_size in enumerate(groupSizes):
            if len(group_candidates[group_size]) == group_size - 1:
                result.append(list(group_candidates[group_size]) + [i])
                group_candidates[group_size] = set()
            else:
                group_candidates[group_size].add(i)
        return result
