"""
Solved and accepted problrm number 10: (Plus One)
Difficulty: easy
"""
class Solution(object):
    def plusOne(self, digits):
        if len(digits) == 0:
            return digits
        else:
            i = len(digits) - 1
            while i >= 0:
                if digits[i] < 9:
                    digits[i] += 1
                    return digits
                else:
                    if i == 0:
                        digits[i] = 1
                        digits.append(0)
                        return digits
                    else:
                        digits[i] = 0
                        i -= 1

                        