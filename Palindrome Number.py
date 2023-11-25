"""
Solved and accepted problrm number 2: (Palindrome Number)
Difficulty: easy
"""

import math

class Solution(object):
    def isPalindrome(self, x):
        res = True
        x_str = str(x)
        j = len(x_str)-1
        for i in range(int(math.floor(len(x_str)/2))):
            if x_str[i] != x_str[j]:
                res = False
                break
            else:
                j -= 1
        return res