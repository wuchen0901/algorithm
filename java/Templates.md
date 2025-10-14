# Algorithm Interview Universal Templates (Java)


> Focus on **generalizable, interview-friendly** patterns with clear invariants. All snippets are compact and meant to
> be adapted quickly.

---

## Templates Overview

| Category | Template | Priority | Frequent Problems |
|----------|----------|----------|-------------------|
| 🧩 1. Sliding Window (Map) | expand + shrink | ⭐⭐⭐⭐ | 3, 76, 567, 438, 209 |
| 🪞 2. Two Pointers (Opposing) | sum / diff / dedupe | ⭐⭐⭐⭐ | 11, 15, 26, 283 |
| 🧮 3. Prefix Sum + HashMap | sum = k / parity / balance | ⭐⭐⭐⭐ | 560, 525, 1248 |
| 🔁 4. Binary Search on Answer | check(mid) monotonic | ⭐⭐⭐⭐ | 875, 1011, 410 |
| 🧱 5. Monotonic Stack / Queue | next greater / histogram | ⭐⭐⭐⭐ | 739, 84, 42 |
| 🪜 6. Heap / Priority Queue | top-K / merge / median | ⭐⭐⭐⭐ | 23, 215, 347 |
| 🧭 7. Greedy (Intervals) | sort by end / start | ⭐⭐⭐ | 435, 452, 56 |
| 🌉 8. BFS / DFS | graph search / islands / maze | ⭐⭐⭐⭐ | 200, 207, 994, 127 |
| 🕸 9. Topological Sort | Kahn / DFS order | ⭐⭐⭐ | 210, 269 |
| ⚙️ 10. Union-Find (DSU) | connected components | ⭐⭐ | 547, 684 |
| 🎯 11. DP Fundamentals (0/1 Knapsack) | dp[i][j] / compression | ⭐⭐⭐⭐ | 416, 518, 474 |
| 💰 12. Advanced DP | LIS / interval / edit | ⭐⭐⭐ | 300, 5, 72 |
| 🌳 13. Tree Recursion Template | post-order merge child info | ⭐⭐⭐⭐ | 543, 124, 236 |
| ⚡ 14. BST + Inorder Logic | validate / kth / build | ⭐⭐ | 98, 230 |
| 🧠 15. Binary Search (Array) | left-right pattern | ⭐⭐⭐⭐ | 34, 74, 162 |

---

## 0) Notation & Tips

* Window `[l, r)` is half-open unless noted; length = `r - l`.
* Prefer **Map counts** over Set for sliding window generality.
* Always state: *invariant*, *shrink/expand condition*, *time/space*.

---

## 1) Sliding Window (Counting Map)

**Use for:** longest/shortest substring/ subarray with frequency constraints.

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

## 2) Two Pointers (Sorted Arrays / Strings)

**Use for:** sorted pair sums, dedup, partitioning, merging.

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

* **Remove duplicates (in-place)**: keep write pointer, compare with previous kept.
* **Partition by predicate**: Dutch National Flag / 3-way partition.

---

## 3) Prefix Sum + HashMap (Subarray Problems)

**Use for:** counts/lengths with sum constraints.

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

* **Longest subarray sum = k**: store earliest index of prefix; for each `pre`, if `pre-k` seen at `j`, length `i-j`.
* **Sum <= k**: often needs monotonic deque over prefix or two pointers for non-negatives.

---

## 4) Monotonic Stack / Monotonic Queue

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

**Use for:** minimize x such that `check(x)` true; typical in scheduling, capacity, radius.

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

### 11.1 0/1 Knapsack (maximize value, capacity W)

```java
int knap01(int[] wt, int[] val, int W) {
    int n = wt.length;
    int[] dp = new int[W + 1];
    for (int i = 0; i < n; i++) for (int c = W; c >= wt[i]; c--) dp[c] = Math.max(dp[c], dp[c - wt[i]] + val[i]);
    return dp[W];
}
```

### 11.2 Unbounded Knapsack (complete)

```java
int unbounded(int[] wt, int[] val, int W) {
    int n = wt.length;
    int[] dp = new int[W + 1];
    for (int i = 0; i < n; i++) for (int c = wt[i]; c <= W; c++) dp[c] = Math.max(dp[c], dp[c - wt[i]] + val[i]);
    return dp[W];
}
```

### 11.3 Coin Change - Min Coins

```java
int coinMin(int[] coins, int amt) {
    int INF = 1_000_000_000;
    int[] dp = new int[amt + 1];
    Arrays.fill(dp, INF);
    dp[0] = 0;
    for (int c : coins) for (int a = c; a <= amt; a++) dp[a] = Math.min(dp[a], dp[a - c] + 1);
    return dp[amt] >= INF ? -1 : dp[amt];
}
```

### 11.4 Coin Change - Count Ways (Order-insensitive)

```java
long coinCount(int[] coins, int amt) {
    long[] dp = new long[amt + 1];
    dp[0] = 1;
    for (int c : coins) for (int a = c; a <= amt; a++) dp[a] += dp[a - c];
    return dp[amt];
}
```

### 11.5 LIS (O(n log n)) - Patience

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

### 12.1 KMP (Prefix Function)

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

* Useful for pattern matching and string periodicity; similar role to KMP.

---

## 13) Tree Recursion Template

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
