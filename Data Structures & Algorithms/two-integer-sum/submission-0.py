class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {nums[0]:0}
        indexes = []
        for index,element in enumerate(nums[1:]):
            remaining =  target-element
            if remaining in history:
                indexes.append(history[remaining])
                indexes.append(index+1)
                
                return indexes
            history[element] = index+1
        