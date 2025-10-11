from collections import Counter
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(l + 1)]
        for index in range(1, l + 1):
            s = strs[index - 1]
            counter = Counter(s)
            for i in range(m + 1):
                for j in range(n + 1):
                    dp[index][i][j] = dp[index - 1][i][j]
                    if 0 <= i - counter['0'] and 0 <= j - counter['1']:
                        dp[index][i][j] = max(dp[index][i][j], dp[index - 1][i - counter['0']][j - counter['1']] + 1)

        return dp[l][m][n]


print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
