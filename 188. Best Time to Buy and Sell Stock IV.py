from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        hold = [-float("inf")] * (k + 1)
        cash = [0] * (k + 1)
        for price in prices:
            for i in range(k, 0, -1):
                hold[i - 1] = max(hold[i - 1], cash[i] - price)
                cash[i - 1] = max(cash[i - 1], hold[i - 1] + price)
        return cash[0]


print(Solution().maxProfit(2, [3, 5, 0, 3, 1, 4]))
