class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxnum = 1
        minmax = 1
        for n in nums:
            if n == 0:
                maxnum, minmax = 1, 1
                continue
            temp = maxnum * n
            maxnum = max(n * maxnum, n * minmax, n)
            minmax = min(temp, n * minmax, n)
            res = max(maxnum, res)
        return res