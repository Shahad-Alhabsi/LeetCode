"""
Solved and accepted problrm number 8: (Search Insert Position)
Difficulty: easy
"""

class Solution(object):
    def searchInsert(self, nums, target):
        if target > nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i] >= target:
                    return i
    