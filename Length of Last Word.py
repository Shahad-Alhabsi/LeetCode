"""
Solved and accepted problrm number 9: (Length of Last Word)
Difficulty: easy
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        st = s.split()
        return len(st[-1])