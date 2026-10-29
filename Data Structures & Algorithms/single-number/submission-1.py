from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        countt = Counter(nums)
        for key, value in countt.items():
            if value == 1:
                return key