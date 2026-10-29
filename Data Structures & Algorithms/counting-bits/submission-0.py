class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for idx in range(n+1):
            temp = 0
            while idx:
                temp += idx % 2
                idx = idx >> 1
            res.append(temp)
        return res 