from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        need = Counter(p)
        window = Counter()
        left = right = 0
        while right < len(s):
            c = s[right]
            window[c] += 1
            right += 1
            while window[c] > need[c]:
                window[s[left]] -= 1
                left += 1
            if right - left == len(p):
                res.append(left)
        return res
