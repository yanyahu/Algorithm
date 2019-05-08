# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dict  = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c not in bracket_dict:
                stack.append(c)
            elif not stack or bracket_dict[c] != stack.pop():
                return False
        return not stack