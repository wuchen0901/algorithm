from typing import List, Tuple


class Solution:
    """
    LeetCode 53 – Maximum Subarray

    This template provides:
      1) maxSubArray: classic Kadane – O(n), handles all-negative arrays.
      2) maxSubArray_with_indices: returns (best_sum, left_index, right_index).
      3) compress_runs (optional): merges same-sign runs; can speed up in practice.

    Usage preference:
      - For interviews: use maxSubArray (shortest & most reliable).
      - If you need the actual subarray indices: use maxSubArray_with_indices.
      - compress_runs is optional; correctness is identical without it.
    """

    # ---------- 1) Short & perfect for interviews ----------
    def maxSubArray(self, nums: List[int]) -> int:
        """Return the maximum subarray sum using Kadane's algorithm.
        Works for any integer array (including all-negative), O(n) time, O(1) space.
        """
        cur = best = nums[0]
        for x in nums[1:]:
            # Either extend the previous subarray or start fresh at x
            cur = max(x, cur + x)
            best = max(best, cur)
        return best

    # ---------- 2) Variant that also returns indices ----------
    def maxSubArray_with_indices(self, nums: List[int]) -> Tuple[int, int, int]:
        """Return (best_sum, left, right) for the maximum subarray.
        left/right are inclusive indices in the original array.
        """
        cur_sum = nums[0]
        best_sum = nums[0]
        cur_l = 0
        best_l = 0
        best_r = 0

        for i in range(1, len(nums)):
            x = nums[i]
            # If extending hurts, start from current position
            if cur_sum + x < x:
                cur_sum = x
                cur_l = i
            else:
                cur_sum += x

            if cur_sum > best_sum:
                best_sum = cur_sum
                best_l = cur_l
                best_r = i

        return best_sum, best_l, best_r

    # ---------- 3) Optional: same-sign run compression ----------
    # You usually don't need this in interviews, but it's here for completeness.
    def compress_runs(self, nums: List[int]) -> List[Tuple[int, int, int]]:
        """Compress consecutive same-sign values.
        Returns a list of tuples (run_sum, L, R), where [L, R] are original indices.
        Example: [1, 2, -1, -2, 2] -> [(3,0,1), (-3,2,3), (2,4,4)]
        """
        if not nums:
            return []
        runs: List[Tuple[int, int, int]] = []
        run_sum = nums[0]
        L = R = 0

        for i in range(1, len(nums)):
            x = nums[i]
            if (run_sum >= 0 and x >= 0) or (run_sum < 0 and x < 0):
                run_sum += x
                R = i
            else:
                runs.append((run_sum, L, R))
                run_sum = x
                L = R = i
        runs.append((run_sum, L, R))
        return runs

    def maxSubArray_on_compressed(self, nums: List[int]) -> Tuple[int, int, int]:
        """Run Kadane on compressed runs and return (best_sum, L, R) in original indices.
        Correctness is identical to normal Kadane; may be faster if there are long runs.
        """
        runs = self.compress_runs(nums)
        # Kadane over runs while tracking original indices
        cur_sum, cur_L, cur_R = runs[0]
        best_sum, best_L, best_R = cur_sum, cur_L, cur_R

        for s, L, R in runs[1:]:
            if cur_sum + s < s:  # start new at this run
                cur_sum, cur_L, cur_R = s, L, R
            else:                # extend previous
                cur_sum += s
                cur_R = R

            if cur_sum > best_sum:
                best_sum, best_L, best_R = cur_sum, cur_L, cur_R

        return best_sum, best_L, best_R


if __name__ == "__main__":
    solution = Solution()

    # Basic check (classic Kadane)
    arr = [0, 1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]
    print("Kadane sum:", solution.maxSubArray(arr))

    # Indices variant
    s, l, r = solution.maxSubArray_with_indices(arr)
    print("Kadane with indices:", s, (l, r), "subarray:", arr[l:r+1])

    # Compressed variant (optional)
    s2, l2, r2 = solution.maxSubArray_on_compressed(arr)
    print("Compressed Kadane:", s2, (l2, r2), "subarray:", arr[l2:r2+1])
