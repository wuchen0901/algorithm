# LeetCode High-Frequency Trick Library

> Use this together with `Templates.md`.
> Templates answer "what framework should I try?"
> Tricks answer "what transformation or insight should I try when no template fits cleanly?"

---

## How To Use This Note

When reviewing a problem, force yourself to write these four tags:

- `Category`: array / linked list / tree / graph / dp / math
- `Template`: sliding window / binary search / bfs / dp / ...
- `Trick`: modulo cycle / reverse transform / dummy node / ...
- `Mother Problem`: rotate / interval merge / path aggregation / ...

If the template is weak but the trick is strong, store the problem here instead of marking it as "won't do again".

---

## 1. Modulo Cycle

- Signal: array is circular, indices wrap around, rotate / ring / circular traversal
- Core move: `k %= n`, use `(i + k) % n`
- Typical problems:
  - `189. Rotate Array`
  - circular array variants
- Reminder:
  - always reduce `k`
  - think about whether the problem is logically a ring even if the array is written linearly

---

## 2. Whole Transform, Then Local Repair

- Signal: direct construction is awkward, but a global transform makes the target almost correct
- Core move:
  - reverse all
  - fix prefix
  - fix suffix
- Typical problems:
  - `189. Rotate Array`
- Canonical example:
  - rotate right by `k`
  - reverse whole array
  - reverse first `k`
  - reverse remaining `n - k`

```text
[1,2,3,4,5,6,7], k = 3
reverse all      -> [7,6,5,4,3,2,1]
reverse first 3  -> [5,6,7,4,3,2,1]
reverse rest     -> [5,6,7,1,2,3,4]
```

---

## 3. Two Pointers For In-Place Overwrite

- Signal: remove / keep / deduplicate / move valid values forward
- Core move:
  - one pointer reads
  - one pointer writes
- Typical problems:
  - `26. Remove Duplicates from Sorted Array`
  - `27. Remove Element`
  - `80. Remove Duplicates from Sorted Array II`
  - `283. Move Zeroes`
- Mental model:
  - do not swap unless needed
  - think "compress valid elements"

---

## 4. Fill From The Back

- Signal: writing forward would overwrite data you still need
- Core move:
  - compare from the back
  - place larger / later result at the tail
- Typical problems:
  - `88. Merge Sorted Array`

---

## 5. Sort First, Then The Structure Appears

- Signal: unsorted relations are messy, but relative order is what matters
- Core move:
  - sort first
  - then use pointers / greedy / grouping
- Typical problems:
  - `15. 3Sum`
  - `56. Merge Intervals`
  - `452. Minimum Number of Arrows to Burst Balloons`
  - `435. Non-overlapping Intervals`
- Questions to ask:
  - after sorting, can I scan once?
  - after sorting, can duplicates be handled locally?

---

## 6. Prefix Sum Plus Hash Map

- Signal: subarray sum / balanced state / count of continuous intervals
- Core move:
  - convert interval property into difference of two prefixes
  - store seen prefix states in a map
- Typical problems:
  - `560. Subarray Sum Equals K`
  - `525. Contiguous Array`
- Mental model:
  - interval question -> prefix state question

---

## 7. Dummy Node For Linked Lists

- Signal: head node may be deleted / replaced / reconnected
- Core move:
  - create a fake head
  - let all operations happen after `dummy`
- Typical problems:
  - `19. Remove Nth Node From End of List`
  - `21. Merge Two Sorted Lists`
  - `203. Remove Linked List Elements`
  - `24. Swap Nodes in Pairs`
- Benefit:
  - removes head special-case logic

---

## 8. Fast-Slow Pointer

- Signal: middle / cycle / kth from end / repeated state transition
- Core move:
  - one moves faster than the other
- Typical problems:
  - `141. Linked List Cycle`
  - `142. Linked List Cycle II`
  - `876. Middle of the Linked List`
  - `202. Happy Number`
- Extension:
  - not only linked lists
  - any deterministic "next state" can be viewed as a linked list

---

## 9. Postorder Aggregation On Trees

- Signal: parent answer depends on information from left and right subtrees
- Core move:
  - compute child info first
  - merge at current node
- Typical problems:
  - `110. Balanced Binary Tree`
  - `543. Diameter of Binary Tree`
  - `124. Binary Tree Maximum Path Sum`
- Question to ask:
  - what information should each subtree return upward?

---

## 10. Preorder With Path State

- Signal: path sum / root-to-leaf decisions / path recording
- Core move:
  - carry path information downward
  - undo state on backtrack when needed
- Typical problems:
  - `112. Path Sum`
  - `113. Path Sum II`

---

## 11. Same-Layer Dedup In Backtracking

- Signal: combinations / permutations with duplicates
- Core move:
  - sort first
  - deduplicate on the same tree level
- Typical problems:
  - `40. Combination Sum II`
  - `47. Permutations II`
- Important distinction:
  - same-layer dedup is not the same as same-branch restriction

---

## 12. Count By Right Endpoint

- Signal: counting subarrays in a valid sliding window
- Core move:
  - if window `[l..r]` is valid, then valid subarrays ending at `r` are `r - l + 1`
- Typical problems:
  - `992. Subarrays with K Different Integers`
  - `atMost(K)` family
- Mental model:
  - classify all subarrays by their right endpoint

---

## 13. Binary Search On Boundary, Not Exact Value

- Signal: first >= x, last <= x, insertion point, leftmost / rightmost answer
- Core move:
  - stop trying to find the target directly
  - search for the boundary where the predicate changes
- Typical problems:
  - `34. Find First and Last Position of Element in Sorted Array`
  - `35. Search Insert Position`
  - `704. Binary Search`

---

## 14. Binary Search On Answer

- Signal: minimize the maximum / maximize the minimum / feasible under limit
- Core move:
  - guess an answer
  - write `check(mid)`
  - rely on monotonicity
- Typical problems:
  - `875. Koko Eating Bananas`
  - `1891. Cutting Ribbons`
- Checklist:
  - is there monotonicity?
  - can I validate a candidate in linear time?

---

## 15. Rotated Sorted Array: First Decide Which Half Is Ordered

- Signal: sorted array has been rotated
- Core move:
  - for each mid, judge whether left half or right half is sorted
  - then decide where the target can still lie
- Typical problems:
  - `33. Search in Rotated Sorted Array`
  - `81. Search in Rotated Sorted Array II`

---

## 16. Monotonic Stack: First Greater / First Smaller On One Side

- Signal: for each element, find the next greater / smaller element
- Core move:
  - maintain a stack of candidates that are still useful
- Typical problems:
  - `739. Daily Temperatures`
  - `84. Largest Rectangle in Histogram`
- Mental model:
  - once a new value makes an old candidate impossible to matter again, pop it

---

## 17. BFS Means Shortest Steps In Unweighted Graphs

- Signal: minimum number of moves / transformations / layers
- Core move:
  - use BFS layer order
  - mark visited when enqueuing, not when dequeuing
- Typical problems:
  - `127. Word Ladder`
  - `994. Rotting Oranges`
  - `1091. Shortest Path in Binary Matrix`

---

## 18. Convert A Problem To "Ending At i"

- Signal: dp over subarrays / subsequences / max sum ending here
- Core move:
  - define `dp[i]` as the best answer ending at `i`
- Typical problems:
  - `53. Maximum Subarray`
  - `300. Longest Increasing Subsequence`
- Reminder:
  - a good state definition often matters more than the transition itself

---

## 19. XOR Cancellation

- Signal: pairs cancel, one odd item remains
- Core move:
  - `a ^ a = 0`
  - `a ^ 0 = a`
- Typical problems:
  - `136. Single Number`
- Nature:
  - this is a conclusion-type trick
  - just remember it directly

---

## 20. Details Problems Are Often About Edge Conditions, Not Algorithm Difficulty

- Signal: string to integer / divide without operators / reverse integer
- Core move:
  - isolate sign
  - handle overflow first-class
  - decide boundary cases before coding
- Typical problems:
  - `7. Reverse Integer`
  - `8. String to Integer (atoi)`
  - `29. Divide Two Integers`

---

## 21. Review Template For Each Problem

Use this after solving or failing a problem:

```text
Problem:
Category:
Template:
Trick:
Mother Problem:
Why I missed it:
Key invariant:
One-line takeaway:
```

Example for `189. Rotate Array`:

```text
Problem: 189. Rotate Array
Category: Array
Template: None obvious
Trick: modulo cycle + reverse transform
Mother Problem: cyclic shift / rotation
Why I missed it: kept thinking in direct simulation
Key invariant: reverse(all) -> reverse(prefix k) -> reverse(suffix n-k)
One-line takeaway: rotation can often be rewritten as a reversible transform
```

---

## 22. Priority Tricks To Memorize First

If you only memorize ten, memorize these:

1. `dummy node`
2. `fast-slow pointer`
3. `in-place overwrite`
4. `modulo cycle`
5. `reverse transform`
6. `sort first`
7. `prefix sum + hash`
8. `same-layer dedup`
9. `postorder aggregation`
10. `monotonic stack`

