class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        n = len(s)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                sub = s[i:j + 1]
                if sub == sub[::-1] and len(sub) > len(res):
                    res = sub
        return res
