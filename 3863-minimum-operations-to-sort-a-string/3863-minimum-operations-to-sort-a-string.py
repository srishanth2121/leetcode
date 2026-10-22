class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        # Check if the string is already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
            
        # If length is 2 and not sorted, it's impossible because any proper substring is of length 1
        if n == 2:
            return -1
            
        mn, mx = min(s), max(s)
        min_idx = s.find(mn)
        max_idx = s.rfind(mx)
        
        # If the minimum character is already at the start, or the maximum character is at the end
        if min_idx == 0 or max_idx == n - 1:
            return 1
            
        # If the maximum character is at the start and the minimum is at the end, it takes 3 operations
        if min_idx == n - 1 and max_idx == 0:
            return 3
            
        # Otherwise, it can be done in 2 operations
        return 2