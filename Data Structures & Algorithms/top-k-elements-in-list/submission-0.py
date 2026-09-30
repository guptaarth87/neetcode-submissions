from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count frequencies
        # nums = [1, 1, 1, 2, 2, 3] -> {1: 3, 2: 2, 3: 1}
        counts = Counter(nums)
        
        # Step 2: Create buckets where index represents frequency (0 to len(nums))
        # buckets = [[], [], [], [], [], [], []]
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Step 3: Fill buckets based on frequency
        # Number 1 has freq 3 -> put 1 in buckets[3]
        # Number 2 has freq 2 -> put 2 in buckets[2]
        # Number 3 has freq 1 -> put 3 in buckets[1]
        for num, freq in counts.items():
            buckets[freq].append(num)
            
        # Step 4: Traverse buckets from highest frequency to lowest
        result = []
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
                    
        return result