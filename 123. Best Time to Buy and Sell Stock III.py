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


print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
