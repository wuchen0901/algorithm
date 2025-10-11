from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -float('inf')
        cash = 0

        for price in prices:
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - fee)

        return cash


print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))
