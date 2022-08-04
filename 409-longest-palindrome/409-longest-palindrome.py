class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = collections.Counter(s)
        palindrome_length = 0
        odd = False
        for key, value in letters.items():
            if value % 2 == 0:
                palindrome_length += value
            else:
                odd = True
                palindrome_length += value - 1
        if odd:
            palindrome_length += 1
        return palindrome_length
            