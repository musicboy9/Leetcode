"""
Runtime
38
ms

Beats
52.92%
of users with Python3

Memory
16.53
MB

Beats
69.94%
of users with Python3
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

        