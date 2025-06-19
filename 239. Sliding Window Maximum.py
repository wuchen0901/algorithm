from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        deque = []
        for i in range(k):
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)

        result = []
        result.append(nums[deque[0]])
        for i in range(l - k ):
            if deque[0] == i:
                deque.pop(0)
            while deque and nums[deque[-1]] < nums[i + k]:
                deque.pop()
            deque.append(i + k)
            result.append(nums[deque[0]])
        return result


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([8, 2, 7, 1, 4, 5, 3], 3))
