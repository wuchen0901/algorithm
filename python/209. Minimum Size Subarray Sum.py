# Sliding Window Conventions 滑动窗口的惯例
# 1. Use [left, right) interval: left inclusive, right exclusive.
#    使用 [left, right) 区间：左闭右开。
# 2. Expand the window by moving 'right' forward (add nums[right], then right += 1).
#    扩展窗口：移动 right 指针（加入 nums[right]，然后 right += 1）。
# 3. Shrink the window by moving 'left' forward when the constraint is violated.
#    收缩窗口：当条件不满足时，移动 left 指针。
# 4. Window length is always (right - left).
#    窗口长度始终是 (right - left)。
# 5. Update the answer in the correct place:
#    - For minimum length problems: after shrinking while valid.
#    - For maximum length problems: while the window is valid.
#    更新答案的时机：
#    - 最小长度问题：在收缩之后仍然满足条件时更新。
#    - 最大长度问题：窗口满足条件时更新。

#	•	窗口边界：定义区间边界，语义强 → 推荐 用完立即更新。
#	•	工作变量：普通循环索引，语义弱 → 跟随循环结构更新即可。
from math import inf
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = right = 0
        total = 0
        minimal_length = inf
        # Input: target = 7, nums = [2,3,1,2,4,3]
        # Output: 2
        while right < n:
            total += nums[right]
            right += 1
            while target <= total:
                minimal_length = min(minimal_length, right - left)
                total -= nums[left]
                left += 1
        return 0 if minimal_length == inf else minimal_length
