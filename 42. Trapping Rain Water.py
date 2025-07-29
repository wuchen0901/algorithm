from typing import List


class Solution:
    def trap_stack(self, height: List[int]) -> int:
        stack = []
        water = 0
        # stack是为了找配对。类似parentheses
        for right in range(len(height)):
            while stack and height[right] > height[stack[-1]]:
                bottom = stack.pop()
                if stack:
                    left = stack[-1]
                    width = right - left - 1
                    bounded_height = min(height[left], height[right]) - height[bottom]
                    water += width * bounded_height

            stack.append(right)

        return water

    def trap_two_pointers(self, height: List[int]) -> int:
        # two pointers point at 0
        # 平移第二个指针
        # *
        # *                     *
        # *                     *       *
        # *           * *       *       *
        # *   *   * * * *   *   * *   * *
        # * * * * * * * * * * * * * * * *
        #
        # left = 1
        # right = 3
        #
        # left = right = 0
        # find next position of 'right' which is greater or equal to height[left]
        # while right < len(height) and height[left] <= height[right]:
        #     right += 1
        # 我觉得两个指针，应该是要找到一个范围，算出water，然后移动两个指针到下一个位置计算水
        # But how to move two pointers?
        # Two pointers move inward?
        # To calculate water, left and right should be at left and right shores
        # If we move left and right separately, then using two pointers is meaningless
        # 难道应该先假设充满了水，然后再减去留不住的水？
        # 用左右两个指针，只能算出来它们之间能装的水
        # 然后移动短的一侧？目的是排除掉多余的水
        # 每一次移动，是不是至少应该对结果有一点贡献？好像不一定，有序数组求和就不需要
        # 一定不是靠单个指针分别移动，单独计算自己经过的区域储存的水
        # 也不是用这两个指针找成对的位置，不能根据它们的和来制订移动策略，而且这种策略的目的是为了寻找一对一对的位置，而本题肯定不是找一个位置或者寻找所有一对一对的位置
        # 它肯定是在遍历的过程中不断的累积结果
        # 但是这个结果靠一个指针自己肯定是完成不了的，如果可以的话，那根本就不需要两个指针
        # 所以只可能是两个指针之间存水的量 和 当前这个值不断进行区域的加减法
        # 举个例子
        #
        # *
        # *   *
        # * * *
        # min(3,2) * 1 - 1 = 1
        # 这种方式确实是有效的，但是还是那个问题，就是left right必须是站在岸边
        # *
        # *
        # *   *
        # * * * * *
        # 难道应该一直向中心找递增的数？
        # 比如最开始是0, 4
        # 变成0, 2
        #
        #
        #           *   *
        #   * *     * * *
        # * * * *   * * * *
        # left = 2, right = 7
        # 然后再inward traverse的时候，去掉blocks就可以了
        # water = 4 * 2 = 8
        # 水位 = 2
        # left or right, which one moves first doesn't matter.
        # When they move to a smaller value, subtract the value.
        # left moves to 3, height[3] = 1
        # water -= 1 ( at most 水位)
        # water = 7
        # right也向inward移动
        # right[6] = 2
        # check if it is higher than water level
        # left and right always find value higher than water level
        # left moves to the right to right?
        # I get that, always move the shorter side
        #
        #               *
        #     *         *
        # *   *         *
        # *   *   *     *   *
        # *   * * * * * * * *
        left, right = 0, len(height) - 1
        water = 0
        level = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < level:
                    water += level - height[left]
                else:
                    level = height[left]
                left += 1
            else:
                if height[right] < level:
                    water += level - height[right]
                else:
                    level = height[right]
                right -= 1
        return water
