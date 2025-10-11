from collections import defaultdict
from typing import List, Counter, Dict


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        count = 0

        def backtrack(curr: List[int], start: int):
            nonlocal count
            if amount < sum(curr):
                if amount == sum(curr):
                    count += 1
                return

            for i in range(start, len(curr)):
                curr.append(curr[i])
                backtrack(curr, i)
                curr.pop()

        backtrack([], 0)
        return count

    def change_v2(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        coins.sort()
        dp: List[List[int]] = [[0] * len(coins) for _ in range(amount + 1)]
        for i, n in enumerate(coins):
            if n <= amount:
                dp[n][i] = 1

        for i in range(amount):
            for j in range(len(coins)):
                for index, coin in enumerate(coins):
                    if j <= index:
                        if i + coin <= amount:
                            dp[i + coin][index] += dp[i][j]

        return sum(dp[amount])

    def change_v3(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j]
                if 0 <= j - coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]

        return dp[n][amount]


print(Solution().change_v3(10, [2, 3, 5]))
print(Solution().change_v2(10, [2, 3, 5]))
print(Solution().change_v2(0, []))
print(Solution().change_v2(5000, [1, 2]))
print(Solution().change(5000, [1, 2]))
