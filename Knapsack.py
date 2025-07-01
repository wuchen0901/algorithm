from typing import List


def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    num_items = len(weights)
    max_value = 0

    def backtrack(start: int, total_weight: int, total_value: int):
        nonlocal max_value
        if total_weight > capacity:
            return

        max_value = max(max_value, total_value)

        for i in range(start, num_items):
            backtrack(i + 1, total_weight + weights[i], total_value + values[i])

    backtrack(0, 0, 0)
    return max_value
