class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        s = "0123456789"
        word_count = 2
        word_length = 2
        '''
        
        if len(words) == 0 or len(words[0]) == 0:
            return []
        
        # init
        window_start = 0
        word_frequency = {}
        result = []
        
        word_count = len(words)
        word_length = len(words[0])
        
        # track frequency of current words
        for word in words:
            if word not in word_frequency:
                word_frequency[word] = 0
            word_frequency[word] += 1
            
        # loop through the array - we only need to go len() - word_count * word_length times
        for i in range(len(s) - word_count * word_length + 1):
            # track all the words I've seen to track duplicates
            words_seen = {}
            
            # find the next word
            for j in range(0, word_count):
                next_word_index = i + j * word_length
                next_word = s[next_word_index : next_word_index + word_length]
                
                if next_word not in word_frequency:
                    break
                
                if next_word not in words_seen:
                    words_seen[next_word] = 0
                words_seen[next_word] += 1
                
                if words_seen[next_word] > word_frequency[next_word]:
                    break
            
                if j + 1 == word_count:
                    result.append(i)
                
        return result
        