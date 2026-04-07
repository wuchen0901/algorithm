# Algorithm Interview Universal Templates (Java)

> Focus on **generalizable, interview-friendly** patterns with clear invariants. All snippets are compact and meant to
> be adapted quickly.

---

## Templates Overview

| Category | Template | Priority |
|----------|----------|----------|
| [🧩 1. Sliding Window](#1-sliding-window) | expand + shrink | ⭐⭐⭐⭐ |
| [🪞 2. Two Pointers](#2-two-pointers) | opposing / same direction | ⭐⭐⭐⭐ |
| [🧮 3. Prefix Sum](#3-prefix-sum) | range sum / subarray state | ⭐⭐⭐⭐ |
| [🔁 4. Binary Search on Answer](#5-binary-search-value-space--answer) | check(mid) monotonic | ⭐⭐⭐⭐ |
| [🧱 5. Monotonic Stack / Queue](#4-monotonic-stack--monotonic-queue) | next greater / histogram | ⭐⭐⭐⭐ |
| [🪜 6. Heap / Priority Queue](#7-heap--k-way-merge) | top-K / merge / median | ⭐⭐⭐⭐ |
| [🧭 7. Greedy (Intervals)](#6-greedy---intervals) | sort by end / start | ⭐⭐⭐ |
| [🌉 8. BFS / DFS](#8-graph-bfsdfs) | graph search / islands / maze | ⭐⭐⭐⭐ |
| [🕸 9. Topological Sort](#10-topological-sort-kahn) | Kahn / DFS order | ⭐⭐⭐ |
| [⚙️ 10. Union-Find (DSU)](#9-union-find-dsu) | connected components | ⭐⭐ |
| [🎯 11. DP Fundamentals (0/1 Knapsack)](#11-dynamic-programming-core-templates) | dp[i][j] / compression | ⭐⭐⭐⭐ |
| [💰 12. Advanced DP](#115-lis-on-log-n---patience) | LIS / interval / edit | ⭐⭐⭐ |
| [🌳 13. Tree Recursion Template](#13-tree-recursion-template) | post-order merge child info | ⭐⭐⭐⭐ |
| [⚡ 14. BST + Inorder Logic](#13-tree-recursion-template) | validate / kth / build | ⭐⭐ |
| [🧠 15. Binary Search (Array)](#5-binary-search-value-space--answer) | left-right pattern | ⭐⭐⭐⭐ |

---

## 0) Notation & Tips

* Window `[l, r)` is half-open unless noted; length = `r - l`.
* Prefer **Map counts** over Set for sliding window generality.
* Always state: *invariant*, *shrink/expand condition*, *time/space*.

---

## 1) Sliding Window

* 入门（固定窗口）：[643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)
* 入门（可变窗口，单一约束）：[209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
* 基础（无重复字符）：[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
* 进阶（频次匹配，是否存在）：[567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)
* 进阶（频次匹配，找全部位置）：[438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
* 高阶（最小覆盖子串，多条件收缩）：[76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
* 高阶（至多 K 种字符）：[340. Longest Substring with At Most K Distinct Characters](#11-problem-spotlight-340-longest-substring-with-at-most-k-distinct-characters)
* 高阶（过渡题，先做 atMost 计数）：[Given `nums = [1,2,1,2,3]`, `k = 2`，统计 `atMost(2)` 的子数组数量](#12-atmost-k-distinct-subarray-count-for-992)
* 高阶（双窗口/至多 K 转化）：[992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)
* [930. Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/)
* [1248. Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/)


### 1.1 Problem Spotlight: 340. Longest Substring with At Most K Distinct Characters

题目内容（总结）：
给定字符串 `s` 和整数 `k`，返回 `s` 中“最多包含 `k` 种不同字符”的最长子串长度。

```java
int lengthOfLongestSubstringKDistinct(String s, int k) {
    Map<Character, Integer> window = new HashMap<>();
    int longestLength = 0;
    int l = 0;
    for (int r = 0; r < s.length(); r++) {
        window.put(s.charAt(r), window.getOrDefault(s.charAt(r), 0) + 1);
        // shink
        while (k < window.size()) {
            window.compute(s.charAt(l), (character, frequency) -> (frequency == null || frequency == 1) ? null : frequency - 1);
            l++;
        }

        if (longestLength < r + 1 - l) {
            longestLength = r + 1 - l;
        }
    }

    return longestLength;
}
```

示例：
* `s = "eceba", k = 2`，答案是 `3`（子串 `"ece"`）
* `s = "aa", k = 1`，答案是 `2`（子串 `"aa"`）

边界：
* 当 `k = 0` 时，答案为 `0`
* 当 `s` 为空串时，答案为 `0`

### 1.2 AtMost K Distinct Subarray Count (for 992)

题目（过渡题）：
给定 `nums = [1,2,1,2,3]`，`k = 2`，统计“至多包含 2 种不同整数”的子数组数量 `atMost(2)`。

核心思路：
* 用滑动窗口维护“窗口内不同整数个数 <= k”
* 当窗口合法时，以 `r` 结尾的合法子数组个数是 `r - l + 1`
* 把每个 `r` 的贡献累加到答案

```java
int atMostKDistinctSubarrays(int[] nums, int k) {
    Map<Integer, Integer> freq = new HashMap<>();
    int l = 0;
    int ans = 0;

    for (int r = 0; r < nums.length; r++) {
        freq.put(nums[r], freq.getOrDefault(nums[r], 0) + 1);
        while (freq.size() > k) {
            int left = nums[l++];
            int c = freq.get(left) - 1;
            if (c == 0) freq.remove(left);
            else freq.put(left, c);
        }
        ans += r - l + 1;
        // 为什么是 r - l + 1 ?
        // 这是一个按“右端点分类计数”的数学思想。
        // 对于数组 [a, b, c, d]，所有子数组可以按“以哪个元素结尾”来统计：
        // 以 a 结尾: [a] -> 1 个
        // 以 b 结尾: [b], [a,b] -> 2 个
        // 以 c 结尾: [c], [b,c], [a,b,c] -> 3 个
        // 以 d 结尾: [d], [c,d], [b,c,d], [a,b,c,d] -> 4 个
        // 总数 = 1 + 2 + 3 + 4 = 10
        //
        // 在滑动窗口中，如果当前合法窗口是 [l..r]，
        // 那么所有以 r 结尾且合法的子数组就是：
        // [r..r], [r-1..r], ..., [l..r]
        // 一共有 r - l + 1 个
        // 因此每次 r 扩展后，可以把 r - l + 1 加到答案里。
    }
    return ans;
}
```

对 `nums = [1,2,1,2,3], k = 2`：
* `atMost(2) = 12`
* `atMost(1) = 5`
* 所以 `exactly(2) = atMost(2) - atMost(1) = 7`

```java
int solve(String s) {
    Map<Character, Integer> win = new HashMap<>();
    int l = 0, ans = 0;
    for (int r = 0; r < s.length(); r++) {
        char c = s.charAt(r);
        win.put(c, win.getOrDefault(c, 0) + 1);    // expand
        while (/* window invalid */) {          // e.g. win.get(c) > 1; or size>k; or need>have
            char x = s.charAt(l++);
            int t = win.get(x) - 1;
            if (t == 0) win.remove(x);
            else win.put(x, t);
        }
        ans = Math.max(ans, r - l + 1);         // or min for shortest
    }
    return ans;
}
```

Variants:

* **At most K distinct**: invalid = `win.size() > K`.
* **Exactly K distinct**: `atMost(K) - atMost(K-1)`.
* **Minimum Window Substring**: maintain `need` and `have/valid` counters; update `ans` only when `valid == need.size()`
  then shrink.
* **Subarray product < K (ints)**: maintain `long prod`; while `prod >= K` shrink.

---

## 2) Two Pointers

**Use for:** opposing scans on sorted arrays / strings, or same-direction scans such as fast-slow pointers.

### 2.1 Opposing

* [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
* [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
* [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
* [15. 3Sum](https://leetcode.com/problems/3sum/)

**Use for:** sorted pair sums, palindrome checks, left-right contraction.

```java
int twoSumClosest(int[] a, int target) {
    Arrays.sort(a);
    int l = 0, r = a.length - 1, best = 1_000_000_000;
    while (l < r) {
        int s = a[l] + a[r];
        best = Math.abs(s - target) < Math.abs(best - target) ? s : best;
        if (s < target) l++;
        else r--;              // move to improve
    }
    return best;
}
```

* **3Sum / 4Sum**: fix one number, then run opposing pointers on the suffix.
* **Container / palindrome**: each round remove the side that cannot improve the answer.

### 2.2 Same Direction

[27. Remove Element](https://leetcode.com/problems/remove-element/)

[283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)

[26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

[876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

[80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

[19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

[287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

[142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

**Use for:** in-place compaction, stable overwrite, fast-slow traversal.

```java
int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int slow = 1;
    for (int fast = 1; fast < nums.length; fast++) {
        if (nums[fast] != nums[slow - 1]) {
            nums[slow++] = nums[fast];
        }
    }
    return slow;
}
```

* **Move zeroes / remove element**: `fast` scans, `slow` writes the next kept position.
* **Linked list middle / cycle**: both pointers move forward, but at different speeds.
* **Sliding window** is also same-direction pointers, but is split into section 1 because it has its own expand-shrink invariant.

---

## 3) Prefix Sum

核心作用：把“子数组 / 区间”问题转换成“两个前缀状态之间的关系”。

### 3.1 Prefix Sum Array

**适用场景：** 静态区间和、快速回答 `sum(l..r)`、二维积分图。

**题型标签：** Prefix Sum

```java
int[] buildPrefixSum(int[] nums) {
    int[] pre = new int[nums.length + 1];
    for (int i = 0; i < nums.length; i++) {
        pre[i + 1] = pre[i] + nums[i];
    }
    return pre;
}

int rangeSum(int[] pre, int left, int right) {
    return pre[right + 1] - pre[left];
}
```

* **识别信号**: 多次查询区间和，数组本身不频繁修改。
* **核心公式**: `sum(l..r) = pre[r + 1] - pre[l]`
* **常见延伸**: 2D prefix sum, difference array

### 3.2 Prefix Sum + HashMap

**适用场景：** 子数组计数、最长子数组、前缀状态匹配。

**题型标签：** Prefix Sum

**模板标签：** Prefix Sum + HashMap

例题：

* [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
* [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/)
* [1248. Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/)

```java
int subarraySumEqualsK(int[] nums, int k) {
    Map<Integer, Integer> cnt = new HashMap<>();
    cnt.put(0, 1);
    int pre = 0, ans = 0;
    for (int x : nums) {
        pre += x;
        ans += cnt.getOrDefault(pre - k, 0);
        cnt.put(pre, cnt.getOrDefault(pre, 0) + 1);
    }
    return ans;
}
```

* **识别信号**: 问“有多少个子数组”“最长多长”“是否存在某种平衡状态”
* **核心转化**: 当前前缀 `pre` 需要去历史里找 `pre - target` 或“相同状态”
* **560**: 查 `pre - k` 出现多少次
* **525**: 查某个前缀状态最早出现的位置
* **1248**: 把“奇数个数”当作前缀状态，再查 `pre - k`
* **补充**: `sum <= k` 往往不是这个模板，常见是双指针（非负数组）或前缀和 + 单调队列

---

## 4) Monotonic Stack / Monotonic Queue

[739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

[84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

[42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

[239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

**Next Greater Element / Histogram / Daily Temperatures**

```java
int[] nextGreater(int[] a) {
    int n = a.length;
    int[] ans = new int[n];
    Arrays.fill(ans, -1);
    Deque<Integer> st = new ArrayDeque<>(); // store indices, a[st] strictly decreasing
    for (int i = 0; i < n; i++) {
        while (!st.isEmpty() && a[i] > a[st.peek()]) ans[st.pop()] = i;
        st.push(i);
    }
    return ans; // indices or values as needed
}
```

**Sliding Window Maximum (Monotonic Deque)**

```java
int[] maxWindow(int[] a, int k) {
    int n = a.length;
    int[] res = new int[n - k + 1];
    int j = 0;
    Deque<Integer> dq = new ArrayDeque<>(); // store indices, a[dq] decreasing
    for (int i = 0; i < n; i++) {
        while (!dq.isEmpty() && dq.peekFirst() <= i - k) dq.pollFirst();
        while (!dq.isEmpty() && a[dq.peekLast()] <= a[i]) dq.pollLast();
        dq.offerLast(i);
        if (i >= k - 1) res[j++] = a[dq.peekFirst()];
    }
    return res;
}
```

---

## 5) Binary Search (Value Space / Answer)

[1891. Cutting Ribbons](https://leetcode.com/problems/cutting-ribbons/)

[875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

[1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

[410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)

**Use for:** minimize x such that `check(x)` true; typical in scheduling, capacity, radius.

```java
// 100m stick, cut into equal integer lengths, at least k pieces.
// Find the maximum feasible piece length.
int maxLen(int k) {
    int l = 1, r = 100, ans = -1;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (100 / mid >= k) { // feasible, try larger length
            ans = mid;
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return ans;
}
```

```java
int bsMinTrue(int lo, int hi) { // [lo, hi] inclusive
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (check(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
```

`check(mid)` must be **monotonic**.

---

## 6) Greedy - Intervals

[435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

[452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

[56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

**Non-overlapping intervals / min arrows / scheduling**

```java
int eraseOverlap(int[][] itv) {
    Arrays.sort(itv, (a, b) -> a[1] == b[1] ? a[0] - b[0] : a[1] - b[1]);
    int cnt = 0, end = Integer.MIN_VALUE;
    for (int[] x : itv) {
        if (x[0] >= end) {
            cnt++;
            end = x[1];
        }
    }
    return itv.length - cnt; // removals
}
```

Greedy by **earliest finish** (classic theorem).

---

## 7) Heap / K-Way Merge

[23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

[215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

[295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

**Use for:** merge k sorted lists/arrays, top-K, streaming median.

```java
List<Integer> mergeK(List<int[]> lists) {
    PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));
    for (int i = 0; i < lists.size(); i++) if (lists.get(i).length > 0) pq.offer(new int[]{lists.get(i)[0], i, 0});
    List<Integer> out = new ArrayList<>();
    while (!pq.isEmpty()) {
        int[] cur = pq.poll();
        out.add(cur[0]);
        int i = cur[1], j = cur[2];
        if (j + 1 < lists.get(i).length) pq.offer(new int[]{lists.get(i)[j + 1], i, j + 1});
    }
    return out;
}
```

* **Top-K frequent**: frequency map plus heap (size K) or bucket sort.

---

## 8) Graph BFS/DFS

[200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

[994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

[127. Word Ladder](https://leetcode.com/problems/word-ladder/)

[207. Course Schedule](https://leetcode.com/problems/course-schedule/)

**Grid BFS (shortest path in unweighted graphs)**

```java
int bfs(int[][] g, int sx, int sy) {
    int m = g.length, n = g[0].length;
    boolean[][] vis = new boolean[m][n];
    int[][] d = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    Deque<int[]> q = new ArrayDeque<>();
    q.offer(new int[]{sx, sy});
    vis[sx][sy] = true;
    int steps = 0;
    while (!q.isEmpty()) {
        for (int sz = q.size(); sz > 0; sz--) {
            int[] p = q.poll();
            int x = p[0], y = p[1];
            if (/* target cond */) return steps;
            for (int[] v : d) {
                int nx = x + v[0], ny = y + v[1];
                if (0 <= nx && nx < m && 0 <= ny && ny < n && !vis[nx][ny] &&/* passable */true) {
                    vis[nx][ny] = true;
                    q.offer(new int[]{nx, ny});
                }
            }
        }
        steps++;
    }
    return -1;
}
```

**Dijkstra (non-negative weights)**

```java
int[] dijkstra(List<int[]>[] g, int s) { // g[u]: {v,w}
    int n = g.length;
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[s] = 0;
    PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
    pq.offer(new int[]{s, 0});
    boolean[] vis = new boolean[n];
    while (!pq.isEmpty()) {
        int[] cur = pq.poll();
        int u = cur[0];
        if (vis[u]) continue;
        vis[u] = true;
        for (int[] e : g[u]) {
            int v = e[0], w = e[1];
            if (dist[u] != Integer.MAX_VALUE && dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                pq.offer(new int[]{v, dist[v]});
            }
        }
    }
    return dist;
}
```

---

## 9) Union-Find (DSU)

[547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)

[684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)

[721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)

**Use for:** connectivity, components, Kruskal MST, islands.

```java
class DSU {
    int[] p, r;

    DSU(int n) {
        p = new int[n];
        r = new int[n];
        for (int i = 0; i < n; i++) p[i] = i;
    }

    int find(int x) {
        return p[x] == x ? x : (p[x] = find(p[x]));
    }

    boolean unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (r[a] < r[b]) {
            int t = a;
            a = b;
            b = t;
        }
        p[b] = a;
        if (r[a] == r[b]) r[a]++;
        return true;
    }
}
```

---

## 10) Topological Sort (Kahn)

[210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

[269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)

[207. Course Schedule](https://leetcode.com/problems/course-schedule/)

**Use for:** DAG order, course schedule.

```java
List<Integer> topo(int n, List<Integer>[] g) {
    int[] indeg = new int[n];
    for (int u = 0; u < n; u++) for (int v : g[u]) indeg[v]++;
    Deque<Integer> q = new ArrayDeque<>();
    for (int i = 0; i < n; i++) if (indeg[i] == 0) q.offer(i);
    List<Integer> order = new ArrayList<>();
    while (!q.isEmpty()) {
        int u = q.poll();
        order.add(u);
        for (int v : g[u]) if (--indeg[v] == 0) q.offer(v);
    }
    return order.size() == n ? order : Collections.emptyList();
}
```

---

## 11) Dynamic Programming Core Templates

[416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

[518. Coin Change II](https://leetcode.com/problems/coin-change-ii/)

[474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/)

[72. Edit Distance](https://leetcode.com/problems/edit-distance/)

| 模板函数声明 | 题目                                                                                                                                                                                                             | 硬币能否无限取 | 目标                        | 重复面额 |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|---------------------------|------|
| `int coinCount01(int[] coins, int amount)` | [Given coins [2,1,6,8,5], how many ways are there to make up a total of 8? (each coin can be used at most once; combinations, order does not matter; see 11.4.2)](#1142-2d-dp-template-01-knapsack-count-ways) | 否       | count ways / combinations | 否（若输入有重复面额，需先定义按“硬币实例”还是按“面额”计数） |
| `int coinCountUnbounded(int[] coins, int amount)` | [Given coins [2,1,6,8,5], how many ways are there to make up a total of 8? (coins can be reused; combinations, order does not matter; see 11.4.1)](#1141-2d-dp-template-unbounded-knapsack-count-ways)         | 是       | count ways / combinations | 否    |
| `int coinCountUnboundedPermutations(int[] coins, int amount)` | [377. Combination Sum IV](#1143-1d-dp-template-unbounded-knapsack-count-ways-order-sensitive--permutations) | 是       | count ways / permutations | 否    |
| `int coinChangeUnboundedMin(int[] coins, int amount)` | [322. Coin Change](#1131-unbounded-knapsack)                                                                                                                                                         | 是       | min coins                  | 否    |
| `int coinChange01Min(int[] coins, int amount)` | [322. Coin Change + 硬币不能重复使用的限制](#1132-01-knapsack)                                                                                                                                                  | 否       | min coins                  | 否    |
| `boolean canMakeUnbounded(int[] coins, int amount)` | [Coin Change Feasibility](#1144-feasibility-can-make-amount-01--unbounded) | 是       | feasibility / can make | 否 |
| `boolean canMake01(int[] coins, int amount)` | [Subset/0-1 Feasibility](#1144-feasibility-can-make-amount-01--unbounded) | 否       | feasibility / can make | 否 |
| `int coinCountBounded(int[] coins, int[] limit, int amount)` | [Bounded Knapsack Count Ways](#1145-bounded-knapsack-count-ways-each-coin-has-a-limit) | 否（有上限） | count ways / combinations | 否 |
| `int coinCountUnboundedExactK(int[] coins, int amount, int k)` | [Count Ways with Exactly K Coins](#1146-count-ways-with-exactly-k-coins-unbounded-combinations) | 是 | count ways with exactly k coins | 否 |

### 11.1 0/1 Knapsack (maximize value, capacity W)

* [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
  这道题类似于[ 1, 2, 3, 6, 7, 8] 每种硬币就一个，有几种方法能凑出7? 0/1 knapsack counting problem

  dp[0][0] = 1;
* [494. Target Sum](https://leetcode.com/problems/target-sum/)
  这道题和 416 几乎是一样的
* [474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/)

```java
int knap01(int[] wt, int[] val, int W) {
    int n = wt.length;
    int[] dp = new int[W + 1];
    for (int i = 0; i < n; i++) for (int c = W; c >= wt[i]; c--) dp[c] = Math.max(dp[c], dp[c - wt[i]] + val[i]);
    return dp[W];
}
```

### 11.2 Unbounded Knapsack (complete)

**对应 LeetCode 题目（链接）：**

* [322. Coin Change](https://leetcode.com/problems/coin-change/) 无限硬币，最少硬币数量。最小值版本。完全背包（Unbounded
  Knapsack）的最小值版本标准解法就是动态规划（DP）
* [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/) unbounded knapsack counting problem.
  无限硬币，凑出某个值的方案数
* [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)

```java
int unbounded(int[] wt, int[] val, int W) {
    int n = wt.length;
    int[] dp = new int[W + 1];
    for (int i = 0; i < n; i++) for (int c = wt[i]; c <= W; c++) dp[c] = Math.max(dp[c], dp[c - wt[i]] + val[i]);
    return dp[W];
}
```

### 11.3 Coin Change - Min Coins

#### 11.3.1 Unbounded knapsack

**对应 LeetCode 题目（链接）：** [322. Coin Change](https://leetcode.com/problems/coin-change/)

```java
public int coinChangeUnboundedMin(int[] coins, int amount) {
    int[][] dp = new int[coins.length + 1][amount + 1];

    int inf = amount + 1;

    for (int j = 1; j < amount + 1; j++) {
        dp[0][j] = inf;
    }

    for (int i = 1; i < coins.length + 1; i++) {
        int coin = coins[i - 1];
        for (int j = 1; j < amount + 1; j++) {
            if (0 <= j - coin) {
                // 从 “不用当前 coin：凑成 j 的最少硬币数” 和 “用当前 coin（可重复使用）：凑成 j - coin 的最少硬币数 + 1” 两种方案中取最小值。
                dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - coin] + 1);
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    return dp[coins.length][amount] < inf ? dp[coins.length][amount] : -1;
}
```

#### 11.3.2 0/1 knapsack

[322. Coin Change](https://leetcode.com/problems/coin-change/) 每种硬币只能用一次的时候

```java
// 0/1 knapsack 硬币数量有限
public int coinChange01Min(int[] coins, int amount) {
    int[][] dp = new int[coins.length + 1][amount + 1];

    int inf = amount + 1;

    for (int j = 1; j < amount + 1; j++) {
        dp[0][j] = inf;
    }

    for (int i = 1; i < coins.length + 1; i++) {
        int coin = coins[i - 1];
        for (int j = 1; j < amount + 1; j++) {
            if (0 <= j - coin) {
                // 从 “不用当前 coin：凑成 j 的最少硬币数” 和 “用当前 coin 一次：凑成 j - coin 的最少硬币数 + 1” 两种方案中取最小值。
                dp[i][j] = Math.min(dp[i - 1][j], dp[i - 1][j - coin] + 1);
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    return dp[coins.length][amount] < inf ? dp[coins.length][amount] : -1;
}
```

### 11.4 Coin Change - Count Ways (Order-insensitive)

[518. Coin Change II](https://leetcode.com/problems/coin-change-ii/)

题型：`Unbounded Knapsack`（完全背包，组合数 / 不计顺序）

关键区别（组合数 vs 排列数）：
* **组合数（order-insensitive）**：先枚举 `coin`，再枚举 `amount`
* **排列数（order-sensitive）**：先枚举 `amount`，再枚举 `coin`

```java
public int change(int amount, int[] coins) {
    int[][] dp = new int[coins.length + 1][amount + 1];

    for (int i = 0; i < coins.length + 1; i++) {
        dp[i][0] = 1;
    }

    for (int i = 1; i < coins.length + 1; i++) {
        int coin = coins[i - 1];
        for (int j = 1; j < amount + 1; j++) {
            if (0 <= j - coin) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - coin];
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    return dp[coins.length][amount];
}
```

#### 11.4.1 2D DP Template (Unbounded Knapsack, count ways)

适用题型：`coins = [2,1,6,8,5]`，问“有多少种方法可以凑出总和为 `8`？”（硬币可重复使用；组合数，不计顺序）。

```java
int coinCountUnbounded(int[] coins, int amount) {
    int[][] dp = new int[coins.length + 1][amount + 1];

    // 凑出 0 元只有 1 种方法：什么都不选
    for (int i = 0; i <= coins.length; i++) {
        dp[i][0] = 1;
    }

    for (int i = 1; i <= coins.length; i++) {
        int coin = coins[i - 1];
        for (int j = 1; j <= amount; j++) {
            dp[i][j] = dp[i - 1][j];              // 不用当前硬币
            if (j - coin >= 0) {
                dp[i][j] += dp[i][j - coin];      // 用当前硬币（可重复使用）
            }
        }
    }

    return dp[coins.length][amount];
}
```

#### 11.4.2 2D DP Template (0/1 Knapsack, count ways)

适用题型：`coins = [2,1,6,8,5]`，问“有多少种方法可以凑出总和为 `8`？”（每个硬币最多使用一次；组合数，不计顺序）。

```java
int coinCount01(int[] coins, int amount) {
    int[][] dp = new int[coins.length + 1][amount + 1];

    // 凑出 0 元只有 1 种方法：什么都不选
    for (int i = 0; i <= coins.length; i++) {
        dp[i][0] = 1;
    }

    for (int i = 1; i <= coins.length; i++) {
        int coin = coins[i - 1];
        for (int j = 1; j <= amount; j++) {
            dp[i][j] = dp[i - 1][j];                // 不用当前硬币
            if (j - coin >= 0) {
                dp[i][j] += dp[i - 1][j - coin];    // 用当前硬币（只能用一次）
            }
        }
    }

    return dp[coins.length][amount];
}
```

#### 11.4.3 1D DP Template (Unbounded Knapsack, count ways, order-sensitive / permutations)

[377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)

```java
int coinCountUnboundedPermutations(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    dp[0] = 1;

    // 先枚举 amount，再枚举 coin：统计的是排列数（顺序敏感）
    for (int j = 1; j <= amount; j++) {
        for (int coin : coins) {
            if (j - coin >= 0) {
                dp[j] += dp[j - coin];
            }
        }
    }

    return dp[amount];
}
```

#### 11.4.4 Feasibility (can make amount, 0/1 + unbounded)

适用题型：只问“能不能凑出 amount”，不关心方案数/最小值。

```java
boolean canMakeUnbounded(int[] coins, int amount) {
    boolean[] dp = new boolean[amount + 1];
    dp[0] = true;

    // 完全背包：每种 coin 可重复使用
    for (int coin : coins) {
        for (int j = coin; j <= amount; j++) {
            dp[j] |= dp[j - coin];
        }
    }
    return dp[amount];
}

boolean canMake01(int[] coins, int amount) {
    boolean[] dp = new boolean[amount + 1];
    dp[0] = true;

    // 0/1 背包：每种 coin 只能用一次（倒序）
    for (int coin : coins) {
        for (int j = amount; j >= coin; j--) {
            dp[j] |= dp[j - coin];
        }
    }
    return dp[amount];
}
```

#### 11.4.5 Bounded Knapsack (count ways, each coin has a limit)

适用题型：每种硬币最多可使用 `limit[i]` 次，问组合数（不计顺序）。

```java
int coinCountBounded(int[] coins, int[] limit, int amount) {
    int n = coins.length;
    int[][] dp = new int[n + 1][amount + 1];
    dp[0][0] = 1;

    for (int i = 1; i <= n; i++) {
        int coin = coins[i - 1];
        int cap = limit[i - 1];
        for (int j = 0; j <= amount; j++) {
            dp[i][j] = dp[i - 1][j]; // 不用当前 coin
            for (int k = 1; k <= cap && j - k * coin >= 0; k++) {
                dp[i][j] += dp[i - 1][j - k * coin];
            }
        }
    }
    return dp[n][amount];
}
```

#### 11.4.6 Count Ways with Exactly K Coins (unbounded, combinations)

适用题型：硬币可重复，问“恰好用 `k` 枚硬币凑出 `amount`”的组合数（不计顺序）。

```java
int coinCountUnboundedExactK(int[] coins, int amount, int k) {
    int[][][] dp = new int[coins.length + 1][amount + 1][k + 1];

    for (int i = 0; i < coins.length + 1; i++) {
        dp[i][0][0] = 1;
    }

    for (int i = 1; i < coins.length + 1; i++) {
        int coin = coins[i - 1];
        for (int j = 1; j < amount + 1; j++) {
            for (int c = 1; c < k + 1; c++) {
                dp[i][j][c] = dp[i - 1][j][c];
                if (0 <= j - coin) {
                    dp[i][j][c] += dp[i][j - coin][c - 1];
                }
            }
        }
    }
    return dp[coins.length][amount][k];
}

int coinCountUnboundedExactK(int[] coins, int amount, int k) {
    int[][] dp = new int[k + 1][amount + 1];
    dp[0][0] = 1;

    // 先 coin 后 amount：组合数
    for (int coin : coins) {
        for (int j = coin; j <= amount; j++) {
            for (int c = 1; c <= k; c++) {
                dp[c][j] += dp[c - 1][j - coin];
            }
        }
    }
    return dp[k][amount];
}
```

### 11.5 LIS (O(n log n)) - Patience

[300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

[354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)

```java
int lis(int[] a) {
    int[] d = new int[a.length];
    int len = 0;
    for (int x : a) {
        int i = Arrays.binarySearch(d, 0, len, x);
        if (i < 0) i = -(i + 1);
        d[i] = x;
        if (i == len) len++;
    }
    return len;
}
```

### 11.6 Edit Distance

[72. Edit Distance](https://leetcode.com/problems/edit-distance/)

[583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)

```java
int edit(String a, String b) {
    int m = a.length(), n = b.length();
    int[][] dp = new int[m + 1][n + 1];
    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++)
            dp[i][j] = a.charAt(i - 1) == b.charAt(j - 1) ? dp[i - 1][j - 1]
                    : 1 + Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1]));
    return dp[m][n];
}
```

---

## 12) String Algorithms

[28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

[459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)

### 12.1 KMP (Prefix Function)

[28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

[459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)

```java
int[] lps(char[] p) {
    int n = p.length, i = 1, len = 0;
    int[] lps = new int[n];
    while (i < n) {
        if (p[i] == p[len]) lps[i++] = ++len;
        else if (len > 0) len = lps[len - 1];
        else lps[i++] = 0;
    }
    return lps;
}

boolean kmp(String s, String pat) {
    char[] a = s.toCharArray(), p = pat.toCharArray();
    int[] l = lps(p);
    int i = 0, j = 0;
    while (i < a.length) {
        if (a[i] == p[j]) {
            i++;
            j++;
            if (j == p.length) return true;
        } else if (j > 0) j = l[j - 1];
        else i++;
    }
    return false;
}
```

### 12.2 Z-Function (optional)

[2223. Sum of Scores of Built Strings](https://leetcode.com/problems/sum-of-scores-of-built-strings/)（可用
Z-Function）

* Useful for pattern matching and string periodicity; similar role to KMP.

---

## 13) Tree Recursion Template

**对应 LeetCode 题目（链接）：
** [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/), [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/), [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

**Post-order combine children then return info to parent**

```java
class Info {
    int something;
    boolean ok;
}

Info dfs(TreeNode u) {
    if (u == null) return new Info();
    Info L = dfs(u.left), R = dfs(u.right);
    Info cur = new Info();
    // combine L and R and u
    return cur;
}
```

Common tasks: diameter, BST check, path sum, LCA (with parent returns), etc.

---

## 14) Bitmask DP (TSP-like, small N)

**对应 LeetCode 题目（链接）：
** [847. Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/), [1125. Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/)

```java
int tsp(int[][] w) {
    int n = w.length, N = 1 << n, INF = 1_000_000_000;
    int[][] dp = new int[N][n];
    for (int[] row : dp) Arrays.fill(row, INF);
    dp[1][0] = 0; // start at 0
    for (int m = 1; m < N; m++)
        for (int u = 0; u < n; u++)
            if (((m >> u) & 1) == 1 && dp[m][u] < INF)
                for (int v = 0; v < n; v++)
                    if (((m >> v) & 1) == 0)
                        dp[m | 1 << v][v] = Math.min(dp[m | 1 << v][v], dp[m][u] + w[u][v]);
    int ans = INF;
    for (int u = 0; u < n; u++) ans = Math.min(ans, dp[N - 1][u] + w[u][0]);
    return ans;
}
```

---

## 15) Sweep Line (Events)

[253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

[218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

[732. My Calendar III](https://leetcode.com/problems/my-calendar-iii/)

**Use for:** meeting rooms, max overlap, skyline.

```java
int minRooms(int[][] itv) {
    int n = itv.length;
    int[] s = new int[n], e = new int[n];
    for (int i = 0; i < n; i++) {
        s[i] = itv[i][0];
        e[i] = itv[i][1];
    }
    Arrays.sort(s);
    Arrays.sort(e);
    int i = 0, j = 0, rooms = 0, ans = 0;
    while (i < n) {
        if (s[i] < e[j]) {
            rooms++;
            i++;
            ans = Math.max(ans, rooms);
        } else {
            rooms--;
            j++;
        }
    }
    return ans;
}
```

---

## How to Use in Interviews

1. 先口头给出**问题分类**，然后选模板。
2. 说出**不变式/收缩条件**与**复杂度**。
3. 写核心骨架，再补边界。
4. 如果有优化（如 jump shrink / 二分答案），**口头提及**即可。

> Practice = take 1 new problem, map to one row here, fill in the three slots: *invariant*, *shrink/expand condition*,
*update rule*.
