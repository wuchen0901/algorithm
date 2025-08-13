from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result


if __name__ == '__main__':
    print(0^ 13)
    print(0^ 13^ 13)