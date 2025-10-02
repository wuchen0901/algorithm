from collections import defaultdict
from typing import List, Counter, Dict


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        max_len = amount // min(coins)

        curr: Dict[int, Dict[int, int]] = defaultdict(lambda: defaultdict(int))
        for n in coins:
            curr[n][n] = 1

        cumulative = Counter()

        for s, last_element_to_ways in curr.items():
            cumulative[s] = sum(last_element_to_ways.values())

        for _len in range(2, max_len + 1):
            next_counter: Dict[int, Dict[int, int]] = defaultdict(lambda: defaultdict(int))
            for s, last_element_to_ways in curr.items():
                for last_element, ways in last_element_to_ways.items():
                    for n in coins:
                        if n <= last_element:
                            next_counter[s + n][n] += ways

            if not next_counter:
                break

            for k, v in next_counter.items():
                cumulative[k] += sum(v.values())

        return cumulative[amount]

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


print(Solution().change_v2(0, [1, 2]))
print(Solution().change_v2(0, []))
print(Solution().change_v2(5000, [1, 2]))
print(Solution().change(5000, [1, 2]))
