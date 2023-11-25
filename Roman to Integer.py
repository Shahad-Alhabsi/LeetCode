"""
Solved and accepted problrm number 3: (Roman to Integer)
Difficulty: easy
"""

class Solution(object):
    def romanToInt(self, s):
        sum_ = 0
        values = []
        my_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in s:
            values.append(my_dict[i])
        v = 0
        while v < len(values):
            if v == len(values)-1:
                sum_ += values[v]
                break
            if values[v] >= values[v+1]:
                sum_ += values[v]
                v += 1
            else:
                sum_ += values[v+1] - values[v]
                v += 2
        
        return sum_