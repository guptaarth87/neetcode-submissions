class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grouped = {}
        
        for word in strs:
            # Sorted characters form a unique key for all anagrams
            key = "".join(sorted(word))
            
            # Add word to the key's list
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(word)
        return list(grouped.values())