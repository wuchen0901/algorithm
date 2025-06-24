class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()  # Use a set to track characters in the current window
        left = 0       # Left boundary of sliding window
        right = 0      # Right boundary of sliding window
        max_length = 0 # Result: length of the longest valid substring found so far

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
