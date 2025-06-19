import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num >= heap[0]:
                heapq.heappushpop(heap, num)
        return heap[0]


if __name__ == '__main__':
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
