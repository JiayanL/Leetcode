class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_letters = {}
        t_letters = {}
        
        for i in range(len(s)):
            s_l = s[i]
            t_l = t[i]
            
            if s_l not in s_letters:
                s_letters[s_l] = 0
            s_letters[s_l] += 1
            
            if t_l not in t_letters:
                t_letters[t_l] = 0
            t_letters[t_l] += 1
        
        if s_letters == t_letters:
            return True
        return False