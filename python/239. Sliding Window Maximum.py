from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if k == 1:
        return nums[:]
    if n == 0 or k == 0:
        return []

    dq = deque()  # stores indices, values decreasing
    res = []

    for r in range(n):
        print(r)
        # push: remove smaller/equal elements from back
        while dq and nums[dq[-1]] <= nums[r]:
            dq.pop()
        dq.append(r)

        # evict: remove left-out index
        l = r - k + 1
        if l >= 0 and dq[0] < l:
            dq.popleft()

        # record answer when we have a full window
        if l >= 0:
            res.append(nums[dq[0]])

    return res


print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
