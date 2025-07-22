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
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left if left < len(nums) and nums[left] == target else -1

    def bisect_left(self, nums: List[int], target: int) -> int:
        # [1, 4, 4, 4, 4, 5, 5, 5, 6, 7, 7, 8]
        #  0  1  2  3  4  5  6  7  8  9 10 11
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    s = Solution()
    nums = [1, 4, 4, 4, 4, 5, 5, 5, 6, 7, 7, 8]
    test_cases = [
        (4, 1),
        (5, 5),
        (3, 1),
        (6, 8),
        (0, 0),
        (8, 11),
        (9, 12)
    ]
    for target, expected in test_cases:
        result = s.bisect_left(nums, target)
        print(f"bisect_left(nums, {target}) = {result} | Expected: {expected}")
        assert result == expected, f"Failed on target {target}"
