class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0: return 0
        hold = [float('-inf')] * n
        sold = [float('-inf')] * n
        rest = [0] * n

        hold[0] = -prices[0]  # 第一天买
        # sold[0] = -inf        # 第一天不可能卖
        # rest[0] = 0           # 第一天休息

        for i in range(1, n):
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])
            sold[i] = hold[i - 1] + prices[i]
            rest[i] = max(rest[i - 1], sold[i - 1])

        return max(sold[-1], rest[-1])
