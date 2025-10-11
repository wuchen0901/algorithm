# You are given an array wood where wood[i] represents the length of the i-th wooden stick.
# Your task is to cut these sticks into pieces of equal length, such that you can make at least k pieces in total.
# Find the maximum possible length of each piece that allows you to make at least k pieces.
from itertools import count


# Input: wood = [9, 7, 5], k = 5
# Output: 5
#
# Explanation:
# If you cut each stick into length 5:
# - 9 → one piece of 5
# - 7 → one piece of 5
# - 5 → one piece of 5
#
# You get 3 pieces — not enough.
#
# Try length 3:
# - 9 → 3 pieces
# - 7 → 2 pieces
# - 5 → 1 piece
#
# Total: 6 pieces → ✅ OK
#
# Now binary search for the maximum length that gives at least 5 pieces.
# The answer is 5.


# Function to solve the maximum length to cut wood problem
def maximum_length_to_cut_wood(wood: list[int], k: int) -> int:
    """
    Given an array `wood` where wood[i] represents the length of the i-th wooden stick,
    cut the sticks into pieces of equal length to obtain at least `k` pieces.

    Return the maximum possible length of each piece that allows at least k pieces in total.

    Example:
    Input: wood = [9, 7, 5], k = 5
    Output: 5
    """

    def isOk(l):
        count = 0
        for w in wood:
            count += w // l
        return count >= k

    # 💡 Thinking Tip: In binary search on answers (not indices), never let 'left = 0' when it can cause division by zero.
    # We are searching possible lengths (must be >= 1), so start with left = 1
    left, right = 1, max(wood)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if isOk(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result
