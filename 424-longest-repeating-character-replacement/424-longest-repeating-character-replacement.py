class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initialize our start, max substring count, and the frequency of other characters in our substring
        window_start = 0
        max_repeating_characters = 0
        max_count = 0
        char_freq = {}
        
        # loop through the array
        for i in range(len(s)):
            current_char = s[i]
            
            # log character into my frequency map
            if current_char not in char_freq:
                char_freq[current_char] = 0
            char_freq[current_char] += 1
            
            # choose the character to keep
            max_repeating_characters = max(max_repeating_characters, char_freq[current_char])
            
            # shrink window while there are more than max_repeating + k characters
            while (i - window_start + 1 - max_repeating_characters) > k:
                first_char = s[window_start]
                char_freq[first_char] -= 1
                window_start += 1
            
            # log max
            max_count = max(max_count, i - window_start + 1)
        return max_count
            