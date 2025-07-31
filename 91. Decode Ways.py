class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp1, dp2 = 1, 1
        for i in range(1, len(s)):
            temp = 0
            if s[i] != '0':
                temp = dp2
            two = int(s[i-1:i+1])
            if 10 <= two <= 26:
                temp += dp1
            dp1, dp2 = dp2, temp
        return dp2
