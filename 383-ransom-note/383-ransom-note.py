class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # get letters from magazine
        letters = collections.Counter(magazine)
        
        # check letters in ransomNote
        for c in ransomNote:
            if letters[c] <= 0:
                return False
            letters[c] -= 1
        return True
            