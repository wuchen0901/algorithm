from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        hold = [-float("inf")] * (k + 1)
        cash = [0] * (k + 1)
        for price in prices:
            for i in range(k, 0, -1):
                hold[i - 1] = max(hold[i - 1], cash[i] - price)
                cash[i - 1] = max(cash[i - 1], hold[i - 1] + price)
        return cash[0]

    def maxProfit_dp3d(self, prices: List[int]) -> int:
        """
        Alternative solution using 3D DP: dp[i][t][state]
        i: day index (1..n), t: number of transactions used (0..K),
        state: 0 = HOLD, 1 = CASH
        """
        n = len(prices)
        if n == 0:
            return 0
        K = 2
        HOLD, CASH = 0, 1

        # dp dimensions: (n+1) x (K+1) x 2
        dp = [[[float('-inf'), 0] for _ in range(K + 1)] for _ in range(n + 1)]

        # Base cases for day 0
        for t in range(K + 1):
            dp[0][t][CASH] = 0
            dp[0][t][HOLD] = float('-inf')

        for i in range(1, n + 1):
            price = prices[i - 1]
            # When t == 0, we can only be in CASH with 0 profit
            dp[i][0][CASH] = 0
            dp[i][0][HOLD] = float('-inf')
            for t in range(1, K + 1):
                # Hold: either keep holding, or buy today (consumes one transaction)
                dp[i][t][HOLD] = max(
                    dp[i - 1][t][HOLD],
                    dp[i - 1][t - 1][CASH] - price,
                )
                # Cash: either keep cash, or sell today (does NOT consume a new transaction)
                dp[i][t][CASH] = max(
                    dp[i - 1][t][CASH],
                    dp[i - 1][t][HOLD] + price,
                )

        # Answer: max cash over all t on the last day
        return max(dp[n][t][CASH] for t in range(K + 1))


print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
# Alternative solution call (uncomment to test)
# print(Solution().maxProfit_dp3d([3,3,5,0,0,3,1,4]))
