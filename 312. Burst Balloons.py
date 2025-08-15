import unittest


class Solution:
    def maxCoins(self, nums):
        a = [1] + nums + [1]
        n = len(a)
        dp = [[0] * n for _ in range(n)]

        for length in range(3, n + 1):  # 区间至少 3 才有气球
            for l in range(0, n - length + 1):
                r = l + length - 1
                best = 0
                for k in range(l + 1, r):  # k 是最后戳的气球
                    print(f"dp[{l}][{k}]: {dp[l][k]}")
                    print(f"dp[{k}][{r}]: {dp[k][r]}")
                    print(f"a[{l}] * a[{k}] * a[{r}]:{a[l]} * {a[k]} * {a[r]}: {a[l] * a[k] * a[r]}")
                    best = max(best, dp[l][k] + dp[k][r] + a[l] * a[k] * a[r])
                dp[l][r] = best
                print(f" dp[{l}][{r}]: {dp[l][r]}")

        return dp[0][n - 1]


if __name__ == "__main__":
    print(Solution().maxCoins([3, 1, 5, 8]))
    # 0: 3 1: 15 3:40 4:40
    # 0 - 1: 30 = max(0:3 + 1:15, 3 * 1 * 5 + 3 * 5)
    # 1 - 2: 15 + 24 * 5 = 135 = max( 3 * 1 * 5 + 3 * 5 * 8, 1 * 5 * 8 + 3 * 1 * 8)
    # 2 - 3: 48
    # 0 - 2: 1-2 + 3 * 8 = 159 =

    #     0  1  2  3  4  5
    # a: [1, 3, 1, 5, 8, 1]
    # 1      -> 2      -> 0      -> 3
    # 1      -> 1:2    -> 0:2    -> 0:3
    # [1][3] -> [1][4] -> [0][4] -> [0][5]
    # 15     -> 135    -> 159    -> 167
    # [1][3] -> [1][3] + a[1] * a[3] * a[4] -> [1][4] + a[0] * a[1] * a[4] -> [0][4] + a[0] * a[4] * a[5]
    #                    3    * 5    * 8
    #           [2][4] + a[1] * a[2] * a[4]
    #                    3      1      8
    # [0][2] -> [][] ->

    # 0, 1, 2, 3, 4
