class Solution:
    def lengthOfLongestSubstring_v1(self, s: str) -> int:
        window = set()  # Use a set to track characters in the current window
        left = 0  # Left boundary of sliding window
        right = 0  # Right boundary of sliding window
        max_length = 0  # Result: length of the longest valid substring found so far

        # Sliding window loop: move right boundary to expand the window
        while right < len(s):
            # If s[right] is a duplicate, shrink the window from the left until valid
            if s[right] in window:
                # This inner loop adjusts the left boundary to maintain a valid window
                while s[left] != s[right]:
                    window.remove(s[left])
                    left += 1
                # Remove the duplicate character itself
                window.remove(s[left])
                left += 1

            # "Do something": add current character to window
            window.add(s[right])

            # "Calculate result": after processing s[right], update max_length
            max_length = max(max_length, right - left + 1)

            # Advance right boundary
            right += 1

        return max_length

    def lengthOfLongestSubstring_v2(self, s: str) -> int:
        # key: char, value: index
        window = {}
        left = right = 0
        length = 0
        while right < len(s):
            if s[right] in window:
                left = max(left, window[s[right]] + 1)
            window[s[right]] = right
            right += 1
            # The condition while right < len(s) guarantees safe access to s[right],
            # and the last window’s length must be updated inside the loop (after expansion).
            # If you move that update before reading s[right], you’ll be one step behind.
            length = max(length, right - left)
        return length
