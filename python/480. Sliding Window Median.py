from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        pass


from bisect import bisect_left, insort


def medianSlidingWindow(nums, k):
    window = sorted(nums[:k])
    res = []

    for i in range(k, len(nums) + 1):
        # median
        mid = k // 2
        res.append((window[mid] + window[~mid]) / 2)

        if i == len(nums): break
        # slide: remove old, add new
        old, new = nums[i - k], nums[i]
        window.pop(bisect_left(window, old))
        insort(window, new)
    return res


print(medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
