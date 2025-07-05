from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Greedy solution to remove the minimum number of overlapping intervals.
        Sort intervals by end time, always keep the interval that ends earliest.

        Args:
            intervals (List[List[int]]): List of [start, end] intervals.

        Returns:
            int: Minimum number of intervals to remove.
        """
        if not intervals:
            return 0

        # Step 1: Sort intervals by end time
        intervals.sort(key=lambda x: x[1])

        # Step 2: Initialize
        count = 0
        end = intervals[0][1]  # Track the end of the last added interval

        # Step 3: Iterate through the sorted intervals
        for i in range(1, len(intervals)):
            start, finish = intervals[i]
            if start < end:
                # Overlapping: need to remove this one
                count += 1
            else:
                # No overlap: update the end boundary
                end = finish

        return count
