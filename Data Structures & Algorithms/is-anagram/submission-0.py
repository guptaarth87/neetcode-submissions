from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1_char_frequency = dict(Counter(s))
        string2_char_frequency = dict(Counter(t))
        if string1_char_frequency == string2_char_frequency:
            return True
        else: 
            return False
        
        