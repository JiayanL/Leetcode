class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for i in s:
            if i in valid and len(stack) > 0 and stack[-1] == valid[i]:
                stack.pop()
            else:
                stack.append(i) 
        if stack:
            return False
        return True