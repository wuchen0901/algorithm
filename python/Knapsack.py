"""Legacy aggregator that re-exports knapsack helpers split by category.

The new structure lives inside the ``knapsack`` package:

- ``knapsack.feasibility``          → exact-fill checks (0-1 & unbounded)
- ``knapsack.counting``             → how many ways to reach a target
- ``knapsack.enumeration``          → generate all valid solutions
- ``knapsack.capacity_maximization``→ maximize used weight ≤ W
- ``knapsack.value_maximization``   → maximize total value (classic DP/backtracking)

Importing from this module keeps existing call sites working while pointing
readers to the dedicated modules.
"""

from knapsack.capacity_maximization import (
    knapsack_capacity_max_01,
    knapsack_capacity_max_unbounded,
)
from knapsack.counting import (
    complete_knapsack_count_permutations,
    complete_knapsack_count_ways,
    count_combinations_unbounded_v1,
    count_combinations_unbounded_v3,
    count_combinations_unbounded_v4,
    count_combinations_unbounded_v5,
    count_ordered_sums_unbounded,
    knapsack_count_ways,
)
from knapsack.enumeration import (
    count_combinations_unbounded_v2,
    knapsack_find_all_subsets,
)
from knapsack.feasibility import (
    knapsack_can_fill_01,
    knapsack_can_fill_unbounded,
    knapsack_min_items,
)
from knapsack.value_maximization import (
    knapsack_backtrack_optimized,
    knapsack_combination,
    knapsack_dp_2d,
    knapsack_dp_optimized,
    knapsack_memo_lru_cache,
    knapsack_memo_manual,
    knapsack_v1,
)

__all__ = [
    # Feasibility
    "knapsack_can_fill_01",
    "knapsack_can_fill_unbounded",
    "knapsack_min_items",
    # Counting
    "knapsack_count_ways",
    "complete_knapsack_count_ways",
    "complete_knapsack_count_permutations",
    "count_ordered_sums_unbounded",
    "count_combinations_unbounded_v1",
    "count_combinations_unbounded_v2",
    "count_combinations_unbounded_v3",
    "count_combinations_unbounded_v4",
    "count_combinations_unbounded_v5",
    # Enumeration
    "knapsack_find_all_subsets",
    # Capacity maximization
    "knapsack_capacity_max_01",
    "knapsack_capacity_max_unbounded",
    # Value maximization
    "knapsack_combination",
    "knapsack_backtrack_optimized",
    "knapsack_memo_lru_cache",
    "knapsack_memo_manual",
    "knapsack_dp_2d",
    "knapsack_dp_optimized",
    "knapsack_v1",
]

KNAPSACK_VARIANTS_BY_CATEGORY = {
    "feasibility": [
        knapsack_can_fill_01,
        knapsack_can_fill_unbounded,
        knapsack_min_items,
    ],
    "counting": [
        knapsack_count_ways,
        complete_knapsack_count_ways,
        complete_knapsack_count_permutations,
        count_ordered_sums_unbounded,
        count_combinations_unbounded_v1,
        count_combinations_unbounded_v3,
        count_combinations_unbounded_v4,
        count_combinations_unbounded_v5,
    ],
    "enumeration": [
        knapsack_find_all_subsets,
        count_combinations_unbounded_v2,
    ],
    "capacity_maximization": [
        knapsack_capacity_max_01,
        knapsack_capacity_max_unbounded,
    ],
    "value_maximization": [
        knapsack_combination,
        knapsack_backtrack_optimized,
        knapsack_memo_lru_cache,
        knapsack_memo_manual,
        knapsack_dp_2d,
        knapsack_dp_optimized,
        knapsack_v1,
    ],
}
