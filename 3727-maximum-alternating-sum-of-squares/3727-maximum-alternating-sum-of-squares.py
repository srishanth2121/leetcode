class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Step 1: Square each element and sort in ascending order
        sq = sorted(x * x for x in nums)
        
        # Step 2: Determine the number of negative (odd index) slots
        k = len(nums) // 2
        
        # Step 3: Subtract the smallest squares (negative slots) and add the largest squares (positive slots)
        return sum(sq[k:]) - sum(sq[:k])