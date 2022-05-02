class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for i in s:
            if i in valid and len(stack) > 0:
                if stack[-1] == valid[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i) 
        if stack:
            return False
        return True