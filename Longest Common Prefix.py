"""
Solved and accepted problrm number 4: (Longest Common Prefix)
Difficulty: easy
"""

class Solution(object): 
    def longestCommonPrefix(self,strs):
        pref = ""
        if len(strs) == 0:
            return pref
        elif len(strs) == 1:
            pref = strs[0]
            return pref
        else:
            mini = len(strs[0])
            for word in strs:
                if len(word) < mini:
                    mini = len(word)
            if mini == 0:
                return pref
            else:
                for litter_index in range(mini):
                    for word_index in range(len(strs)-1):
                        if strs[word_index][litter_index] != strs[word_index+1][litter_index]:

                            pref = strs[0][:litter_index]
                            return pref
                        else:                     
                            continue
                    
                        
            pref = strs[0][:litter_index+1]                   
            return pref
        