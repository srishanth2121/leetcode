from math import isqrt

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        
        # Find all divisors of n
        divisors = []
        for i in range(1, isqrt(n) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        for k in divisors:
            valid = True
            blocks = [nums[i:i+k] for i in range(0, n, k)]
            
            # Step 1: Check if each block of size k can be sorted by cyclic rotation
            for b in blocks:
                m = len(b)
                drops = sum(1 for i in range(m) if b[i] > b[(i + 1) % m])
                if drops > 1:
                    valid = False
                    break
            
            if not valid:
                continue
                
            # Step 2: Check if consecutive blocks are in non-decreasing order
            for i in range(len(blocks) - 1):
                if max(blocks[i]) > min(blocks[i+1]):
                    valid = False
                    break
                    
            if valid:
                ans += k
                
        return ans