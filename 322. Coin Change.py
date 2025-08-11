from bisect import bisect_left
from collections import deque
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        summaries = deque([0])
        counts = {0: 0}
        while summaries:
            value = summaries.popleft()
            # 0
            # 4
            for coin in coins:
                # 4
                if value + coin <= amount:
                    # 4 7 11
                    # 4     1
                    # 7     1
                    # 8     2
                    # 11    1
                    #
                    if value + coin in counts:
                        counts[value + coin] = min(counts[value + coin], counts[value] + 1)
                    else:
                        summaries.insert(bisect_left(summaries, value + coin), value + coin)
                        counts[value + coin] = counts[value] + 1

            if value != amount:
                del counts[value]

        return counts.get(amount, -1)
