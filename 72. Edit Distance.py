class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp[i][j] 表示 word1[0..i-1] 到 word2[0..j-1] 的最小编辑距离
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 初始化边界：word1 或 word2 为空串时的距离
        for i in range(m + 1):
            dp[i][0] = i  # 删除所有字符
        for j in range(n + 1):
            dp[0][j] = j  # 插入所有字符

        # 状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # 不需要操作
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1] + 1,  # 替换
                        dp[i][j - 1] + 1,      # 插入
                        dp[i - 1][j] + 1       # 删除
                    )

        return dp[m][n]