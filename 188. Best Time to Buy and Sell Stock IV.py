from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        MAX_TRANSACTION_COUNT = k
        HOLD, SOLD = 0, 1
        dp = [[[-float('inf'), 0] for _ in range(MAX_TRANSACTION_COUNT + 1)] for _ in range(n + 1)]

        for i in range(len(prices)):
            for count in range(MAX_TRANSACTION_COUNT):
                dp[i + 1][count + 1][HOLD] = max(dp[i][count + 1][HOLD], dp[i][count][SOLD] - prices[i])
                dp[i + 1][count + 1][SOLD] = max(dp[i][count + 1][SOLD], dp[i + 1][count + 1][HOLD] + prices[i])

        return dp[n][k][SOLD]


print(Solution().maxProfit(2, [3, 5, 0, 3, 1, 4]))
