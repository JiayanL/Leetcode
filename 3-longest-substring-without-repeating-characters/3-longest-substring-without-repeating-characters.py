class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init start, max_length, and index of the last character
        window_start = 0
        max_length = 0
        char_indices = {}
        
        # loop through string
        for index in range(len(s)):
            current_char = s[index]
            
            # check if current_car is in index
            if current_char in char_indices:
                # either the starting window should be moved up one, or we've already moved past this index, so we can keep this starting window
                window_start = max(window_start, char_indices[current_char] + 1)
            
            # update the last encounter
            char_indices[current_char] = index
            
            # check max length
            max_length = max(max_length, index - window_start + 1)
        return max_length