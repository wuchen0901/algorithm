from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 判断哪一侧是有序的
            if nums[left] <= nums[mid]:  # 左半边有序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # 在左半边
                else:
                    left = mid + 1  # 在右半边
            else:  # 右半边有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # 在右半边
                else:
                    right = mid - 1  # 在左半边

        return -1