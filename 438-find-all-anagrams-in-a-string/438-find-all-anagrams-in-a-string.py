class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # keep track of all letters in p
        chars_to_match = collections.Counter(p)
        
        # easy way to check if all the characters are satisfied in the right frequency
        matched_chars = len(chars_to_match)
        substring_length = len(p)
        
        start, end = 0, 0
        result = []
        # keep track of the amount of letters I've matched
        
        # sliding window
        for end in range(len(s)):
            # process the current character
            char = s[end]
            if char in chars_to_match:
                chars_to_match[char] -= 1
                if chars_to_match[char] == 0:
                    matched_chars -= 1
                    
            if (end - start + 1) != substring_length:
                continue
                
            # when all letters in my window match p, append the start
            if matched_chars == 0:
                result.append(start)
            
            # move the window left by one
            start_char = s[start]
            if start_char in chars_to_match:
                if chars_to_match[start_char] == 0:
                    matched_chars += 1
                chars_to_match[start_char] += 1
            start += 1
        return result