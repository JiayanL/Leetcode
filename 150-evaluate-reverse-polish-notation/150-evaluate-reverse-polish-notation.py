class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # keep a stack of the numbers
        stack = []
        for t in tokens:
            if t not in '+/-*':
                stack.append(t)
            else:
                r, l = int(stack.pop()), int(stack.pop())
                if t == "+":
                    stack.append(l + r)
                elif t == "/":
                    stack.append(int(l/r))
                elif t == "-":
                    stack.append(l - r)
                elif t == "*":
                    stack.append(l * r)
        return stack.pop()