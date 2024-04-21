"""
Runtime
45
ms

Beats
92.46%
of users with Python3

Memory
17.28
MB

Beats
86.74%
of users with Python3
"""

import string
class Solution:
    def rec(self, prefix, s):
        len_s = len(s)
        if s == "":
            return [prefix]
        idx = 0
        while idx < len_s and s[idx] not in self.alphabet:
            idx += 1
        if idx == len_s:
            return [prefix + s]
        
        if s[idx] in self.l_alphabet:
            return self.rec(
                prefix + s[:idx+1],
                s[idx+1:]
            ) + self.rec(
                prefix + s[:idx] + s[idx].upper(),
                s[idx+1:]
            )
        else:
            return self.rec(
                prefix + s[:idx+1],
                s[idx+1:]
            ) + self.rec(
                prefix + s[:idx] + s[idx].lower(),
                s[idx+1:]
            )
        
        

    def letterCasePermutation(self, s: str) -> List[str]:
        self.l_alphabet = set(list(string.ascii_lowercase))
        self.u_alphabet = set(list(string.ascii_uppercase))
        self.alphabet = set()
        self.alphabet.update(self.l_alphabet)
        self.alphabet.update(self.u_alphabet)
        return self.rec("", s)
        
        
        