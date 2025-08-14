from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        for x in nums:
            for i in range(32):
                counts[i] += (x >> i) & 1

        result = 0
        for i in range(32):
            if counts[i] % 3:
                result |= (1 << i)

        # 32 位有符号还原
        if result >= 1 << 31:
            result -= 1 << 32
        return result