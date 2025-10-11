from collections import Counter, defaultdict
from typing import Dict


class Solution:
    """
    LeetCode 76 – Minimum Window Substring

    Sliding Window template (O(|s| + |t|) time, O(|charset|) space).
    Core idea:
      - Expand right to include characters until the window covers all counts in `t`.
      - Then shrink left as much as possible while the window still covers `t`.
      - Track the best (shortest) window.

    Notes:
      - Works for any characters (Unicode-safe) because we use dict/Counter.
      - Handles empty inputs and repeated characters in `t`.
    """

    def minWindow(self, s: str, t: str) -> str:
        # Edge cases
        if not s or not t or len(t) > len(s):
            return ""

        need: Dict[str, int] = Counter(t)         # required counts per char
        window: Dict[str, int] = defaultdict(int) # current window counts

        have_types = 0                             # how many char types currently meet required count
        need_types = len(need)                     # total distinct char types needed

        best_len = float('inf')
        best_start = 0

        left = 0
        for right, ch in enumerate(s):
            # include s[right]
            if ch in need:
                window[ch] += 1
                if window[ch] == need[ch]:
                    have_types += 1

            # shrink from the left while valid (window covers all needed counts)
            while have_types == need_types:
                if (right - left + 1) < best_len:  # update best answer
                    best_len = right - left + 1
                    best_start = left

                left_ch = s[left]
                if left_ch in need:
                    window[left_ch] -= 1
                    if window[left_ch] < need[left_ch]:
                        have_types -= 1
                left += 1

        return "" if best_len == float('inf') else s[best_start: best_start + best_len]


# Optional: a micro-optimized ASCII version using fixed-size arrays.
# Use when the input is guaranteed ASCII to reduce dictionary overhead.
class SolutionASCII:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        need = [0] * 128
        need_types = 0
        for ch in t:
            idx = ord(ch)
            if need[idx] == 0:
                need_types += 1
            need[idx] += 1
        window = [0] * 128
        have_types = 0

        best_len = float('inf')
        best_start = 0

        left = 0
        for right, ch in enumerate(s):
            idx = ord(ch)
            if idx < 128 and need[idx]:
                window[idx] += 1
                if window[idx] == need[idx]:
                    have_types += 1

            while have_types == need_types:
                if (right - left + 1) < best_len:
                    best_len = right - left + 1
                    best_start = left

                left_idx = ord(s[left])
                if left_idx < 128 and need[left_idx]:
                    window[left_idx] -= 1
                    if window[left_idx] < need[left_idx]:
                        have_types -= 1
                left += 1

        return "" if best_len == float('inf') else s[best_start: best_start + best_len]