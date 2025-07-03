from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # ❗Remember:
        # - Use `left <= right` in binary search to ensure the last element is checked.
        # - Update `left = mid + 1` and `right = mid - 1` to avoid infinite loops when `mid == left` or `mid == right`.
        # - This is a classic source of bugs in binary search.
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid

        return -1

    def binary_search_left(self, nums: List[int], target: int) -> int:
        # [1, 4, 4, 4, 4, 5, 5, 5, 6, 7, 7, 8]
        #  0  1  2  3  4  5  6  7  8  9 10 11
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                result = mid
                right = mid - 1

        return result
