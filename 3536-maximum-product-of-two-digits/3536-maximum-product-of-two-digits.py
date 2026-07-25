class Solution:
    def maxProduct(self, n: int) -> int:
        largest = -1
        second_largest = -1

        for digit in  str(n):
            digit = int(digit)

            if digit > largest:
                second_largest = largest
                largest = digit
            elif digit > second_largest:
                second_largest = digit

        return largest * second_largest
        