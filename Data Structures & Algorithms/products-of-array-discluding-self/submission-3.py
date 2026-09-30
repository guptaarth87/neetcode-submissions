import math

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total_product = 1
        zero_count = 0
        
        # Step 1: Count zeros and compute product of all non-zero numbers
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num
                
        # Step 2: Handle cases based on zero_count
        result = []
        for num in nums:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                # Only the position containing 0 gets non-zero product
                result.append(total_product if num == 0 else 0)
            else:
                result.append(total_product // num)
                
        return result
