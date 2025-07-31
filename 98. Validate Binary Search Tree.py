class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 初始化第一行和第一列
        for i in range(m + 1):
            dp[i][0] = i  # word1[:i] -> "" 需要 i 次删除
        for j in range(n + 1):
            dp[0][j] = j  # "" -> word2[:j] 需要 j 次插入

        # 填表
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # 字符相等，不需要操作
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],     # 删除
                        dp[i][j - 1],     # 插入
                        dp[i - 1][j - 1]  # 替换
                    ) + 1

        return dp[m][n]