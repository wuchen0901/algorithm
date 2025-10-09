from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        half_of_total = total // 2
        l = len(stones)
        dp = [[0 for _ in range(half_of_total + 1)] for _ in range(l + 1)]

        for i in range(1, l + 1):
            for s in range(half_of_total + 1):
                stone = stones[i - 1]
                dp[i][s] = dp[i - 1][s]
                if 0 <= s - stone:
                    dp[i][s] = max(dp[i][s],
                                   dp[i - 1][s - stone] + stone)
        return total - 2 * dp[l][half_of_total]


print(Solution().lastStoneWeightII([3, 8, 5, 5]))
