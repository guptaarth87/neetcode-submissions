from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grouped = defaultdict(list)
        print(grouped)
        for stringPattern in strs:
            # Create a 26-count frequency tuple for 'a' through 'z'
            count = [0] * 26
            for char in stringPattern:
                count[ord(char) - ord('a')] += 1
            
            # Tuples are hashable and can be used as dict keys
            grouped[tuple(count)].append(stringPattern)
            
        return list(grouped.values())