class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # count all characters in t
        chars_in_t = collections.Counter(t)
        matched_chars = len(chars_in_t)
        
        min_window_length = len(s) + 1
        result = ""
        
        window_start = 0
        
        # move through all windows
        for window_end in range(len(s)):
            char = s[window_end]
            
            if char in chars_in_t:
                chars_in_t[char] -= 1
                if chars_in_t[char] == 0:
                    matched_chars -= 1
            
            # shrink it
            while matched_chars == 0:
                window_length = window_end - window_start + 1
                if window_length < min_window_length:
                    min_window_length = window_length
                    result = s[window_start:window_end + 1]

                start_char = s[window_start]
                if start_char in chars_in_t:
                    if chars_in_t[start_char] == 0:
                        matched_chars += 1
                    chars_in_t[start_char] += 1
                window_start += 1
                    
        return result