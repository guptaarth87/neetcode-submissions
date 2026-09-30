class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        iterated = []
        nums.sort()
        for i in nums:
            if i in iterated:
                return True
            else:
                iterated.append(i)
        return False
