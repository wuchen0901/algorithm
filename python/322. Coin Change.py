from collections import deque, defaultdict
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        summaries = deque([0])
        counts = {0: 0}
        while summaries:
            value = summaries.popleft()
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
                    summaries.append(value + coin)
                    if value + coin in counts:
                        counts[value + coin] = min(counts[value + coin], counts[value] + 1)
                    else:
                        counts[value + coin] = counts[value] + 1

        return counts.get(amount, -1)

    def coinChange_v2(self, coins: List[int], amount: int) -> int:
        l = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(l + 1)]
        for i in range(l + 1):
            dp[i][0] = 0

        for i in range(1, l + 1):
            coin = coins[i - 1]
            for a in range(amount + 1):
                dp[i][a] = dp[i - 1][a]  # not use coin
                if a - coin >= 0 and dp[i][a - coin] != float('inf'):
                    dp[i][a] = min(dp[i][a], dp[i][a - coin] + 1)

        return -1 if dp[l][amount] == float('inf') else dp[l][amount]


print(Solution().coinChange_v2([1, 4, 6], 12))


class SolutionDP:
    """Dynamic Programming reference solution.
    Time: O(amount * len(coins)), Space: O(amount)
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for c in coins:
            if c <= amount:
                for a in range(c, amount + 1):
                    dp[a] = min(dp[a], dp[a - c] + 1)
        return -1 if dp[amount] == INF else dp[amount]

    def coinChangeV1(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        reachable = {0}  # ✅ 起点
        max_count = amount // min(coins)

        for count in range(1, max_count + 1):
            new_reachable = set()
            for coin in coins:
                # 基于“上一层”的 reachable 扩张到“下一层”
                new_reachable |= {r + coin for r in reachable if r + coin <= amount}
            if amount in new_reachable:
                return count
            reachable = new_reachable  # ✅ 层推进

        return -1


class SolutionBFS:
    """Clean BFS (layered) solution with early exit.
    Time: O(amount * len(coins)) in the worst case, Space: O(amount)
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # Ensure positive coins only
        coins = [c for c in set(coins) if c > 0 and c <= amount]
        if not coins:
            return -1
        from collections import deque
        q = deque([0])
        dist = {0: 0}  # sum -> fewest coins to reach it
        while q:
            v = q.popleft()
            steps = dist[v]
            for c in coins:
                nxt = v + c
                if nxt == amount:
                    return steps + 1
                if 0 <= nxt < amount and nxt not in dist:
                    dist[nxt] = steps + 1
                    q.append(nxt)
        return -1
