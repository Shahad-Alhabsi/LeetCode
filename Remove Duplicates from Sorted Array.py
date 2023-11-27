"""
Solved and accepted problrm number 5: (Remove Duplicates from Sorted Array)
Difficulty: easy
"""

class Solution(object):
    def removeDuplicates(self,nums):
        nums[:] = sorted(set(nums))
        return len(nums)
    