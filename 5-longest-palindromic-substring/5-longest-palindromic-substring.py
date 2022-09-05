class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 2 pointers
        longest_palindrome = ""
        pal_length = 0
        
        for i in range(len(s)):
            # odd case
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > pal_length:
                    pal_length = r - l + 1
                    longest_palindrome = s[l:r+1]
                r += 1
                l -= 1

            # even case
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > pal_length:
                    pal_length = r - l + 1
                    longest_palindrome = s[l:r+1]
                r += 1
                l -= 1
        return longest_palindrome