from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Example: k = 3
        #                     right (=k)
        #                     ↓
        # index:  0   1   2   3   4
        #   arr:  3   2   4   8   7
        # window = [left, right) = [0, 3) → covers indices 0,1,2 → length = 3
        left, right = 0, k
        curr_sum = sum(arr[left:right])
        count = 0
        if threshold * k <= curr_sum:
            count += 1
        while right < len(arr):
            curr_sum += arr[right]
            right += 1
            curr_sum -= arr[left]
            left += 1
            if threshold * k <= curr_sum:
                count += 1
        return count
