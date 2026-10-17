class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        # Create target sorted arrangement based on (digit_sum, value)
        sorted_arr = sorted((digit_sum(x), x) for x in nums)
        
        # Map each target value to its correct index
        target_pos = {val: i for i, (_, val) in enumerate(sorted_arr)}
        
        vis = [False] * n
        swaps = 0
        
        # Find permutation cycles
        for i in range(n):
            if not vis[i]:
                cycle_size = 0
                j = i
                while not vis[j]:
                    vis[j] = True
                    # Move to the position where current element belongs
                    j = target_pos[nums[j]]
                    cycle_size += 1
                if cycle_size > 1:
                    swaps += cycle_size - 1
                    
        return swaps