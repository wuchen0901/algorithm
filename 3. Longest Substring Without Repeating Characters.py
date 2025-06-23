from operator import contains


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        container = set()
        # I should use two indices instead of a queue to implement a sliding window.
        p = 0
        q = 0

        l = 0

        # When should the loop end?
        while q < len(s):
            if s[q] in container:
                l = max(l, q - p)
                # Move p to the one next to the element equals to s[q]
                while s[p] != s[q]:
                    container.remove(s[p])
                    p += 1
                container.remove(s[p])
                p += 1
                # Move q to the one next to s[q]
                container.add(s[q])
                q += 1
            else:
                container.add(s[q])
                q += 1
        return max(l, q - p)
