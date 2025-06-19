class Solution:
    def fib(self, n: int) -> int:
        # There needs to be an array to store fibonacci sequence.
        dp = [0] * n
        # Is n correct?
        # If n = 3:
        # dp = [ 0, 1, 1 ]
        # Then, we need to design a loop to fill the dp array.
        # To fill the array, we need to sum the previous value and the one before it.
        # i
        # dp[i] = dp[i - 2] + dp[i - 1]
        # At last we return dp[-1] + dp[-2]
        # i should start from 2
        # if n = 3, i should end at 2, which is n - 1
        # for i in range(2, n - 1):
        #     dp[i] = dp[i - 2] + dp[i - 1]
        # return dp[-1] + dp[-2]
        # Next, I should handle the edge cases for n.
        # If n = 0, return 0
        # If n = 1, return 1
        # If n = 2, return 1
        if n is 0: return 0
        if n is 1: return 1
        if n is 2: return 1
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[-1] + dp[-2]
