"""
Runtime
998
ms

Beats
58.62%
of users with Python3

Memory
16.68
MB
Beats
29.31%
of users with Python3
"""

class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        
        for num in range(int(10**n)-1, int(10**(n-1)), -1):
            pal = int(str(num) + str(num)[::-1])
            for div in range(int(10**n-1), max(pal//(10**n), int(pal**0.5)), -1):
                if pal % div == 0:
                    return pal % 1337

        