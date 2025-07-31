from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        for num in nums:
            prefix += num
            count += hashmap.get(prefix - k, 0)
            hashmap[prefix] += 1
        return count
