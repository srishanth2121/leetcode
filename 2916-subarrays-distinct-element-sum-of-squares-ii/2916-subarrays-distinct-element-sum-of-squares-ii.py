class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        SHIFT = 40
        MASK = (1 << SHIFT) - 1
        bit = [0] * (n + 1)
        
        def update(idx, val):
            idx += 1
            while idx <= n:
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            idx += 1
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & (-idx)
            return res

        last = {}
        totC = 0
        totS = 0
        g = 0
        ans = 0
        
        for j in range(n):
            v = nums[j]
            p = last.get(v, -1)
            last[v] = j
            
            if p < 0:
                R = totS + totC
            else:
                total_val = query(n - 1)
                p_val = query(p)
                sSuf = (total_val & MASK) - (p_val & MASK)
                cSuf = (total_val >> SHIFT) - (p_val >> SHIFT)
                R = sSuf - p * cSuf
                
                update(p, -((1 << SHIFT) + p))
                totC -= 1
                totS -= p
                
            update(j, (1 << SHIFT) + j)
            totC += 1
            totS += j
            
            g = (g + 2 * R + (j - p)) % MOD
            ans = (ans + g) % MOD
            
        return ans