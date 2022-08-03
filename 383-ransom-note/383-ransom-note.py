class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # get letters from magazine
        letters = {}
        for i in magazine:
            if i not in letters:
                letters[i] = 0
            letters[i] += 1
        
        # check letters in ransomNote
        for i in ransomNote:
            if i not in letters:
                return False
            letters[i] -= 1
            if letters[i] < 0:
                return False
        return True
            