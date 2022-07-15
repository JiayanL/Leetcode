class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # when is s1 a permutation of s2?
        # when s1 and s2 are the same length and s1 has all the same letters as s2
        # thus, first keep track of what letters there are
        
        char_count = {}
        # this keeps track of how many characters I have matched, so I can compare it with the amount of characters in char_count
        matched_characters = 0
        start_index = 0
        
        # log all characters
        for char in s1:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
        
        # now use a sliding window to keep track
        for right_index in range(len(s2)):
            # add the current char to the window
            right_char = s2[right_index]
            
            if right_char in char_count:
                char_count[right_char] -= 1
                if char_count[right_char] == 0:
                    matched_characters += 1
                    
            # check that we have a complete match => anagram
            if matched_characters == len(char_count):
                return True
            
            # decrement the window if I've reached pass the length
            if (right_index + 1) >= len(s1):
                start_char = s2[start_index]
                start_index += 1
                
                if start_char in char_count:
                    if char_count[start_char] == 0:
                        matched_characters -= 1
                    char_count[start_char] += 1
        return False