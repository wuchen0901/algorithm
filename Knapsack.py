from typing import List


# combination-style backtracking
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


# choose/skip-style backtracking
def knapsack_backtrack(weights: List[int], values: List[int], capacity: int) -> int:
    max_value = 0

    def backtrack(path: List[int], index: int):
        nonlocal max_value
        # Prune
        if capacity < sum(weights[i] for i in path):
            return

        # Should I put it here? No — because path is still incomplete (not all choices made).
        # max_value = max(max_value, sum(values[i] for i in path))

        # Choose/skip backtracking ends here.
        if index == len(weights):
            # This is the correct place to evaluate max_value — path is complete.
            max_value = max(max_value, sum(values[i] for i in path))
            return

        backtrack(path, index + 1)

        path.append(index)
        backtrack(path, index + 1)
        path.pop()

    backtrack([], 0)
    return max_value


# choose/skip-style backtracking
def knapsack_backtrack_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    max_value = 0

    def backtrack(index: int, total_weight: int, total_value: int):
        nonlocal max_value
        # Capacity Validation
        if capacity < total_weight:
            return

        # Choose/skip backtracking ends here.
        if index == len(weights):
            max_value = max(max_value, total_value)
            return

        backtrack(index + 1, total_weight, total_value)

        backtrack(index + 1, total_weight + weights[index], total_value + values[index])

    backtrack(0, 0, 0)
    return max_value
