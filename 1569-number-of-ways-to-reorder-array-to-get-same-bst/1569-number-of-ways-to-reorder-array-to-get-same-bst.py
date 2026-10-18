import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def dfs(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # Choose positions for left subtree elements in the combined sequence
            ways = math.comb(len(left) + len(right), len(left)) % MOD
            ways = (ways * dfs(left)) % MOD
            ways = (ways * dfs(right)) % MOD
            
            return ways

        # Subtract 1 because the question asks for reorderings other than the original array
        return (dfs(nums) - 1) % MOD