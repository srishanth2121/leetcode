class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}

        for num in nums1:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        answer = []

        for num in nums2:
            if num in freq and freq[num] >0:
                answer.append(num)
                freq[num] -= 1

        return answer
        