class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # If the required sum exceeds the maximum possible sum of digits, return ""
        if sum > 9 * num:
            return ""
        
        # Maximize the score by packing as many 9s as possible
        nines = sum // 9
        remainder = sum % 9
        
        # Build the string: as many '9's as possible, followed by the remainder digit (if any), 
        # and padded with '0's to match the required length `num`
        if remainder > 0:
            ans = '9' * nines + str(remainder) + '0' * (num - nines - 1)
        else:
            ans = '9' * nines + '0' * (num - nines)
            
        return ans