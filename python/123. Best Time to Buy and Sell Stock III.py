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

    def maxProfitV5(self, prices: List[int]) -> int:
        max_transaction_count = 2
        n = len(prices)
        HOLD, SOLD = 0, 1
        dp = [[[-float('inf'), 0] for _ in range(max_transaction_count + 1)] for _ in range(n + 1)]
        for i in range(len(prices)):
            for k in range(max_transaction_count):
                dp[i + 1][k + 1][HOLD] = max(dp[i][k + 1][HOLD], dp[i][k][SOLD] - prices[i])
                dp[i + 1][k + 1][SOLD] = max(dp[i][k + 1][SOLD], dp[i + 1][k + 1][HOLD] + prices[i])
        return dp[n][max_transaction_count][SOLD]

    def maxProfitV4(self, prices: List[int]) -> int:
        k = 2
        n = len(prices)
        HOLD, SOLD = 0, 1
        dp = [[[-float('inf'), 0] for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(len(prices)):
            dp[i + 1][1][HOLD] = max(dp[i][1][HOLD], dp[i][0][SOLD] - prices[i])
            dp[i + 1][1][SOLD] = max(dp[i][1][SOLD], dp[i + 1][1][HOLD] + prices[i])
            dp[i + 1][2][HOLD] = max(dp[i][2][HOLD], dp[i][1][SOLD] - prices[i])
            dp[i + 1][2][SOLD] = max(dp[i][2][SOLD], dp[i + 1][2][HOLD] + prices[i])

        return dp[n][2][SOLD]

    def maxProfitV3(self, prices: List[int]) -> int:
        k = 2
        n = len(prices)
        HOLD, SOLD = 0, 1
        dp = [[[-float('inf'), 0] for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(len(prices)):
            # 这样写了之后，前两行和后两行之间可以任意交换，但是第一行和第二行，第三行和第四行之间不能任意交换
            # 因为这版把同一天内的状态转移拆成了两对“先买后卖”的小组，而每一对里第二句都依赖第一句刚算出的结果；但两组之间彼此不依赖
            dp[i + 1][1][HOLD] = max(dp[i][1][HOLD], dp[i][2][SOLD] - prices[i])
            dp[i + 1][1][SOLD] = max(dp[i][1][SOLD], dp[i + 1][1][HOLD] + prices[i])
            dp[i + 1][0][HOLD] = max(dp[i][0][HOLD], dp[i][1][SOLD] - prices[i])
            dp[i + 1][0][SOLD] = max(dp[i][0][SOLD], dp[i + 1][0][HOLD] + prices[i])

        return dp[n][0][SOLD]

    def maxProfitV2(self, prices: List[int]) -> int:
        k = 2
        hold = [-float('inf')] * k
        hold[k - 1] = -prices[0]
        sold = [0] * (k + 1)
        for i in range(1, len(prices)):
            # 如果反转这四句话的顺序，答案就错了。
            # 因为计算sold[0]的时候的值，是基于错误的数据hold[0]计算出来的，
            # 此时的hold[0]: -∞只是我们假想的为了计算方便而设置的初始值
            # 但是如果这样做好像也有它的道理，因为这样可以保证一个价格只在一个状态上作用一次，
            # 似乎这种好像更对一些啊？
            # 因为每个hold/sold的值都是基于前一个值计算出来的，
            # 如果倒序过来，那么后续的数据有很多会是基于前面错误的数据计算出来的错数据
            # 只有前面的数据才是正确的，我们要等到前面的正确的数据一步一步把后面错误的数据覆盖掉才行。
            # 但是现实却是把一个price传递下去才是对的呢？
            # 正向去计算的时候，前面的数据也是真的，但是后面的数据纯粹就是复制前面真的数据。
            # 也就是说，过去我们认为，我们是要合并相同remaining transaction count 和相同 state(hold/sold)
            # 但是现在变成了最大值
            # 比如说
            sold[0] = max(sold[0], hold[0] + prices[i])
            hold[0] = max(hold[0], sold[1] - prices[i])
            sold[1] = max(sold[1], hold[1] + prices[i])
            hold[1] = max(hold[1], sold[2] - prices[i])
        return sold[0]

    def maxProfitV1(self, prices: List[int]) -> int:
        k = 2
        hold = [-float('inf')] * k
        hold[k - 1] = -prices[0]
        sold = [0] * (k + 1)
        for i in range(1, len(prices)):
            hold[1] = max(hold[1], sold[2] - prices[i])
            sold[1] = max(sold[1], hold[1] + prices[i])
            hold[0] = max(hold[0], sold[1] - prices[i])
            sold[0] = max(sold[0], hold[0] + prices[i])
        return sold[0]


print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
# Alternative solution call (uncomment to test)
# print(Solution().maxProfit_dp3d([3,3,5,0,0,3,1,4]))
