class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        res = set()
        res.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextRes = set()
            for t in res:
                nextRes.add(t + nums[i])
                nextRes.add(t)
                
            res = nextRes
        if sum(nums) // 2 in res:
            return True
        else:
            return False