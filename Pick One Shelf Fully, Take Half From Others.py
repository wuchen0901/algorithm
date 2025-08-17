# -*- coding: utf-8 -*-
"""
Title: Pick One Shelf Fully, Take Half From Others

You are given an integer array `books`, where `books[i]` is the number of books
on the i-th shelf (0-indexed).

You must choose exactly ONE shelf to take ALL of its books.
From every other shelf, you take HALF of its books.

Return the maximum total number of books you can take.

There are two common interpretations for "half":
1) Real-number half (i.e., x/2.0, allowing fractions)
2) Integer-floor half (i.e., x//2)

Implement both variants.

----------------------------------------------------------------------
Examples
----------------------------------------------------------------------
Example 1 (real half):
Input: books = [4,6,8,2,4,12]
Output: 24.0
Explanation:
Take the entire shelf with 12 (best choice), and half from the others:
12 + (4+6+8+2+4)/2 = 12 + 12 = 24.

Example 2 (real half):
Input: books = [4,6,2]
Output: 9.0
Explanation:
Take 6 fully and half of the others: 6 + (4+2)/2 = 6 + 3 = 9.

Example 3 (floor half):
Input: books = [4,6,2]
Output: 8
Explanation (floor):
Base = 4//2 + 6//2 + 2//2 = 2 + 3 + 1 = 6
Gain if pick 4: 4 - 4//2 = 2
Gain if pick 6: 6 - 6//2 = 3  <-- best
Gain if pick 2: 2 - 2//2 = 1
Answer = 6 + 3 = 9   (if you expect integer output 9)
(If the problem requires integer output, return 9; below we provide both variants.)

----------------------------------------------------------------------
Constraints
----------------------------------------------------------------------
- 1 <= len(books) <= 2 * 10^5
- 0 <= books[i] <= 10^9

----------------------------------------------------------------------
Notes
----------------------------------------------------------------------
This problem has a simple O(n) closed-form solution for the "real half" case:
Let S = sum(books) and M = max(books).
Answer = 0.5 * (S + M)

For the "floor half" case, a standard trick works:
Base = sum(x//2 for x in books)
Gain(i) = x_i - x_i//2 = ceil(x_i/2)
Answer = Base + max_i Gain(i)

For learning DP, we also include a two-state DP that generalizes well to
harder variants (e.g., K shelves taken fully, adjacency constraints, fees).
"""

from typing import List


# ------------------------------------------------------------
# Variant 1: Real-number half (x / 2.0).
# ------------------------------------------------------------

def max_taken_real_fast(books: List[int]) -> float:
    """
    O(n) closed-form:
    Answer = 0.5 * (sum(books) + max(books))
    """
    if not books:
        return 0.0
    return 0.5 * (sum(books) + max(books))


def max_taken_real_dp(books: List[int]) -> float:
    """
    Two-state DP (educational version, also O(n), O(1) space).

    half = total if we have NOT yet used the 'take fully once' option (so all halves so far)
    full = total if we HAVE already used the 'take fully once' option somewhere

    Transition with current x:
      new_half = half + x/2
      new_full = max(full + x/2,  # already used once before, take half now
                     half + x)    # use the 'full' option at this position

    Answer = full after processing all shelves.
    """
    if not books:
        return 0.0

    half = 0.0                # haven't used 'full' yet (all halves so far)
    full = float('-inf')      # already used 'full' (best so far)

    for x in books:
        new_half = half + x / 2.0
        new_full = max(full + x / 2.0, half + x)
        half, full = new_half, new_full

    return full


# ------------------------------------------------------------
# Variant 2: Integer-floor half (x // 2).
# ------------------------------------------------------------

def max_taken_floor_fast(books: List[int]) -> int:
    """
    O(n) solution:
      Base = sum(x//2)
      Gain(i) = x_i - x_i//2 = ceil(x_i/2)
      Answer = Base + max Gain(i)
    """
    if not books:
        return 0
    base = sum(x // 2 for x in books)
    gain = max(x - x // 2 for x in books)  # == ceil(x/2)
    return base + gain


def max_taken_floor_dp(books: List[int]) -> int:
    """
    Two-state DP for floor division variant.

    half = total if we have NOT yet used the 'full' option (sum of x//2 so far)
    full = total if we HAVE already used the 'full' option somewhere (best so far)

    Transition:
      new_half = half + x//2
      new_full = max(full + x//2,   # already used before; half now
                     half + x)      # use full here
    """
    if not books:
        return 0

    half = 0
    full = -10**30  # effectively -inf for ints

    for x in books:
        new_half = half + x // 2
        new_full = max(full + x // 2, half + x)
        half, full = new_half, new_full

    return full


# ------------------------------------------------------------
# Optional: Prefix-sum implementation (your approach)
# (real half). Also O(n), shown for completeness.
# ------------------------------------------------------------

def max_taken_real_prefix(books: List[int]) -> float:
    """
    Your prefix-sum idea:
      For each k as the 'full' shelf:
        total_k = (sum of left)/2 + books[k] + (sum of right)/2
                = 0.5 * S + 0.5 * books[k]
      This reduces to the closed form; still we implement the loop version.
    """
    n = len(books)
    if n == 0:
        return 0.0
    pref = [0] * (n + 1)
    for i, x in enumerate(books):
        pref[i + 1] = pref[i] + x
    S = pref[-1]

    best = float('-inf')
    for k, x in enumerate(books):
        left_half = 0.5 * (pref[k] - pref[0])      # [0..k-1]
        right_half = 0.5 * (S - pref[k + 1])       # [k+1..n-1]
        total = left_half + x + right_half
        if total > best:
            best = total
    return best


# ------------------------------------------------------------
# Quick self-test
# ------------------------------------------------------------
if __name__ == "__main__":
    arr = [4, 6, 8, 2, 4, 12]

    # Real half
    print("Real half (closed-form):", max_taken_real_fast(arr))    # 24.0
    print("Real half (DP)        :", max_taken_real_dp(arr))      # 24.0
    print("Real half (prefix)    :", max_taken_real_prefix(arr))  # 24.0

    # Floor half
    print("Floor half (fast)     :", max_taken_floor_fast(arr))   # base= (2+3+4+1+2+6)=18, best gain=ceil(12/2)=6 -> 24
    print("Floor half (DP)       :", max_taken_floor_dp(arr))     # 24