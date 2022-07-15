class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # similar to finding one anagram but instead of returning true, we return an array
        
        # pattern: a substring of s, s_i is an anagram of p if it's the same length AND has all the same characters
        
        # keep track of the amount of matched characters we have
        matched_chars = 0
        # keep track of the characters
        char_count = {}
        # keep track of our starting window
        window_start = 0
        # keep track of indices of all our anagrams
        result = []
        
        # now populate char_count
        for char in p:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
        
        # find all anagrams
        for window_end in range(len(s)):
            right_char = s[window_end]
            
            # check that this character composes an anagram
            if right_char in char_count:
                char_count[right_char] -= 1
                # check that we have a complete char match
                if char_count[right_char] == 0:
                    matched_chars += 1
            
            # check that we've matched all characters
            if matched_chars == len(char_count):
                result.append(window_start)
            
            # make sure we don't exceed the length of the pattern - this is the case as long as we've surpassed the length of the pattern
            if (window_end + 1) >= len(p):  
                first_char = s[window_start]
                window_start += 1                
                
                # add it back to the hash map and decrement complete match
                if first_char in char_count:
                    if char_count[first_char] == 0:
                        matched_chars -= 1
                    char_count[first_char] += 1
                    
        return result