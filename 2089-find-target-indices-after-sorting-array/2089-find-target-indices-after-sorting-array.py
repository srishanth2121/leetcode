class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Step 1: Sort the array in non-decreasing order
        nums.sort()
        
        # Step 2: Find and return all indices where the element equals target
        return [i for i, x in enumerate(nums) if x == target]


