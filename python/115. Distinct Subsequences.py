"""
LeetCode 115. Distinct Subsequences
Count the number of distinct subsequences of s which equals t.

Approach: 1D DP (O(|s|*|t|) time, O(|t|) space)
- dp[j] = number of ways to form t[:j] using a prefix of s processed so far
- Initialize dp[0] = 1 (empty string is a subsequence of any string in exactly one way)
- For each character ch in s, update dp from right to left over t to avoid overwriting
  the previous row values needed for the transition.

Transition:
  if ch == t[j-1]:
      dp[j] += dp[j-1]

Edge cases handled:
- t == "": answer = 1
- len(s) < len(t): answer = 0 (early exit)
"""

from typing import List

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if n == 0:
            return 1  # empty t is subsequence of any s
        if m < n:
            return 0  # not enough chars to form t

        # dp[j] = ways to form t[:j] using processed prefix of s; dp[0] = 1
        dp: List[int] = [0] * (n + 1)
        dp[0] = 1

        for ch in s:
            # iterate t backwards so dp[j-1] is from previous row
            for j in range(n, 0, -1):
                if ch == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.numDistinct("rabbbit", "rabbit"))  # 3
    print(sol.numDistinct("babgbag", "bag"))     # 5
    print(sol.numDistinct("", ""))               # 1
    print(sol.numDistinct("abc", ""))            # 1
    print(sol.numDistinct("", "a"))              # 0