class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            left = right = i
            res += self.helper(s, left, right)
            res += self.helper(s, left, right + 1)
        return res
    def helper(self,s, left, right):
        res = 0
        while left >= 0 and right < len(s) and s[right] == s[left]:
            res += 1
            left -= 1
            right += 1  
        return res
        