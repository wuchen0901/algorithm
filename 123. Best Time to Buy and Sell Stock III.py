from typing import List
import unittest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        hold = [-float('inf')] * k  # [-inf, -inf]
        hold[k - 1] = -prices[0]  # [-inf, -1]
        cash = [0] * (k + 1)  # [0, 0, 0]
        for i in range(1, len(prices)):  # - - - - - - - - 1  2  3  4  5
            hold[1] = max(hold[1], cash[2] - prices[i])  #-1 -1 -1 -1 -1
            cash[1] = max(cash[1], hold[1] + prices[i])  # 0  1  2  3  4
            hold[0] = max(hold[0], cash[1] - prices[i])  # - -1 -1 -1 -1
            cash[0] = max(cash[0], hold[0] + prices[i])  # 0  1  2  3  4
        return cash[0]
        # k      hold                            cash
        # 0      max(hold[0], cash[1] - price)   max(cash[0], hold[0] + price)
        # 1      max(hold[1], cash[2] - price)   max(cash[1], hold[1] + price)
        # 2                                      0

        #
        #  1        2       1 3 2 8
        #  *-1,1    *-1,1
        #  *-1,1      1,1
        #   0,2       0,2
        #   0,2     *-2,1


print(Solution().maxProfit([1, 2, 3, 4, 5]))
