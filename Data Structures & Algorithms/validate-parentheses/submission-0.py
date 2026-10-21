from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        pairs = { ")" : "(" , "}" : "{", "]" : "["}
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return not stack 
