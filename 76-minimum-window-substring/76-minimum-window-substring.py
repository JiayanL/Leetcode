class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # init tracker of window start and character frequency
        window_start = 0
        matched_chars = 0 
        char_frequency = {}
        
        min_length = len(s) + 1
        result = ""
        
        # track the frequency of my characters
        for char in t:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1
            
        # go through s until we have matched
        for window_end in range(len(s)):
            right_char = s[window_end]
            
            # check if right_char is one of the characters we're looking for
            if right_char in char_frequency:
                char_frequency[right_char] -= 1
                if char_frequency[right_char] == 0:
                    matched_chars += 1
                    
            # decrease the window size while I have complete matches
            while matched_chars == len(char_frequency):
                # check that we have a smaller elngth
                if (window_end - window_start + 1) < min_length:
                    min_length = window_end - window_start + 1
                    result = s[window_start:window_end + 1]
                left_char = s[window_start]
                window_start += 1
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched_chars -= 1
                    char_frequency[left_char] += 1
        return result