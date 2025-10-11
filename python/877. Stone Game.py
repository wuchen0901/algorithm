from typing import List


class Solution:
    def stoneGame(self, piles: List[int]):
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for length in range(2, n + 1):
            for l in range(n - length):
                r = l + length - 1
                dp[l][r] = max(piles[l] - dp[l + 1][r],
                               piles[r] - dp[l][r - 1])
        # 先手赢当且仅当分差 > 0；对 877 总是 True
        return dp[0][n - 1] > 0
