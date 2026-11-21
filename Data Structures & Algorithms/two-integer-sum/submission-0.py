class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_before = {}

        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen_before:
                return [seen_before[complement], i]
            else:
                seen_before[num] = i
        
        return False
        