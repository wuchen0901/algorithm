from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Given a sorted list of integers `numbers` and a target integer `target`,
        returns the 1-based indices of two numbers such that they add up to the target.
        Assumes exactly one solution exists.
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]
