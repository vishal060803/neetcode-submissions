class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
    def helper(self,value):
        n = len(value)

        if n == 1:
            return value[0]
        if n == 2:
            return max(value[0], value[1])

        dp = [0] * (n+1)
        dp[0] = value[0]
        dp[1] = max(value[0], value[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + value[i])
        return dp[n - 1]