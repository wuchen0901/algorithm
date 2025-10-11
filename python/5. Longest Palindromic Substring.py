class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        for i in range(len(s)):
            width = 0
            while 0 <= (i - width) and (i + width) < len(s) and s[i - width] == s[i + width]:
                width += 1
            width -= 1

            length = width * 2 + 1
            if len(longest_palindrome) < length:
                longest_palindrome = s[i - width:i + width + 1]

            if i + 1 < len(s) and s[i] == s[i + 1]:
                width = 0

                while 0 <= (i - width) and (i + 1 + width) < len(s) and s[i - width] == s[i + 1 + width]:
                    width += 1
                width -= 1

                length = width * 2 + 2
                if len(longest_palindrome) < length:
                    longest_palindrome = s[i - width: i + 1 + width + 1]

        return longest_palindrome
