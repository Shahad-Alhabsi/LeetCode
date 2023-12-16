"""
Solved and accepted problrm number 11: (Sqrt(x))
Difficulty: easy
"""

class Solution(object):
    def mySqrt(self, x):
        sqr = str(sqrt(x)).split(".")[0]
        return int(sqr)