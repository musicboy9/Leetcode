"""
Runtime
87
ms

Beats
69.06%
of users with Python3

Memory
19.62
MB

Beats
76.36%
of users with Python3
"""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_anagrams_map = defaultdict(list)
        for word in strs:
            sorted_str_anagrams_map["".join(sorted(word))].append(word)
        return list(sorted_str_anagrams_map.values())
