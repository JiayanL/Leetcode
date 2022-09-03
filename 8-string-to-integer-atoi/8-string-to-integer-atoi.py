class Solution:
    def myAtoi(self, s: str) -> int:
        # deterministic finite automaton
        
        # state 0 -> whitespace
        
        # state 1 -> sign
        
        # state 2 -> integer
        
        """
        state 0 -> state 0, state 1, or state 2
        state 1 -> state 2 or return 0
        state 2 -> state 2 or break
        """
        
        if len(s) == 0:
            return 0
        
        # run state machine
        position = 0
        state = 0
        value = 0
        sign = 1
        while position < len(s):
            char = s[position]
            
            # while we have whitespace
            if state == 0:
                if char == " ":
                    state = 0
                elif char == "+" or char == "-":
                    state = 1
                    sign = 1 if char == "+" else -1
                elif char.isdigit():
                    state = 2
                    value = value * 10 + int(char)
                else:
                    return 0
                
                    
            elif state == 1:
                if char.isdigit():
                    state = 2
                    value = value * 10 + int(char)        
                else:
                    print("2")
                    return 0
                
            elif state == 2:
                if char.isdigit():
                    state = 2
                    value = value * 10 + int(char)
                else:
                    print("3")
                    break
            
            position += 1
        
        value = sign * value
        value = max(-pow(2, 31), value)
        value = min(pow(2, 31) - 1, value)
    
        return value