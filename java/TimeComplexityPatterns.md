# Time Complexity Patterns (Java)

> Use Java code snippets to recognize common time complexity patterns quickly.
> Focus on loop count, recursion depth, and the cost of each operation.

---

## 1. O(1)

```java
int x = nums[0];
int y = x + 1;
return y;
```

- Constant number of operations.
- Does not grow with input size `n`.

---

## 2. O(n)

```java
for (int i = 0; i < n; i++) {
    doSomething();
}
```

- The loop runs `n` times.
- If `doSomething()` is `O(1)`, total time is `O(n)`.

Another common form:

```java
int i = 0;
while (i < n) {
    doSomething();
    i++;
}
```

---

## 3. O(n^2)

```java
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        doSomething();
    }
}
```

- Outer loop runs `n` times.
- Inner loop also runs `n` times each round.
- Total work is `n * n = O(n^2)`.

Typical variant:

```java
for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
        doSomething();
    }
}
```

- Exact count is about `n * (n - 1) / 2`.
- Drop constants and lower-order terms, so still `O(n^2)`.

---

## 4. O(n^3)

```java
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        for (int k = 0; k < n; k++) {
            doSomething();
        }
    }
}
```

- Three nested loops over `n`.
- Total work is `n * n * n = O(n^3)`.

---

## 5. O(log n)

```java
int left = 0;
int right = n - 1;
while (left <= right) {
    int mid = left + (right - left) / 2;
    if (check(mid)) {
        right = mid - 1;
    } else {
        left = mid + 1;
    }
}
```

- Each iteration removes about half of the search space.
- Number of iterations is about `log2(n)`.
- Binary search is the classic `O(log n)` pattern.

Another common form:

```java
for (int i = 1; i < n; i *= 2) {
    doSomething();
}
```

- `i` doubles each round: `1, 2, 4, 8, ...`
- Number of rounds is `O(log n)`.

---

## 6. O(n log n)

```java
for (int i = 0; i < n; i++) {
    int left = 0;
    int right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (check(mid)) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
}
```

- Outer loop: `O(n)`
- Inner binary-search style loop: `O(log n)`
- Total time: `O(n log n)`

Classic examples:

- Merge sort: `O(n log n)`
- Heap sort: `O(n log n)`
- Sorting with comparison-based algorithms is often `O(n log n)`

---

## 7. O(sqrt(n))

```java
for (int i = 1; i * i <= n; i++) {
    doSomething();
}
```

- `i` only goes up to `sqrt(n)`.
- Common in factor checking and primality-related loops.

---

## 8. O(2^n)

```java
void dfs(int index) {
    if (index == n) {
        return;
    }
    dfs(index + 1);
    dfs(index + 1);
}
```

- Each state branches into 2 choices.
- Total nodes in the recursion tree are about `2^n`.
- Common in brute-force subset recursion.

Example meaning:

- pick / not pick
- use / skip

---

## 9. O(n!)

```java
void permute(List<Integer> path, boolean[] used) {
    if (path.size() == n) {
        return;
    }
    for (int i = 0; i < n; i++) {
        if (used[i]) {
            continue;
        }
        used[i] = true;
        path.add(nums[i]);
        permute(path, used);
        path.remove(path.size() - 1);
        used[i] = false;
    }
}
```

- Number of permutations of `n` distinct elements is `n!`.
- Common in permutation generation problems.

---

## 10. O(m + n)

```java
int i = 0;
int j = 0;
while (i < m && j < n) {
    if (a[i] < b[j]) {
        i++;
    } else {
        j++;
    }
}
```

- Pointer `i` moves at most `m` times.
- Pointer `j` moves at most `n` times.
- Total time is `O(m + n)`.

Common in:

- merge two sorted arrays
- two pointers across two inputs
- BFS/DFS graph traversal: `O(V + E)`

---

## 11. O(V + E) in Graphs

```java
Queue<Integer> queue = new LinkedList<>();
boolean[] visited = new boolean[n];
queue.offer(start);
visited[start] = true;

while (!queue.isEmpty()) {
    int node = queue.poll();
    for (int next : graph[node]) {
        if (visited[next]) {
            continue;
        }
        visited[next] = true;
        queue.offer(next);
    }
}
```

- Each vertex is processed at most once.
- Each edge is examined at most once or twice depending on representation.
- BFS and DFS are typically `O(V + E)`.

---

## 12. O(n) Amortized in Sliding Window / Two Pointers

```java
int left = 0;
for (int right = 0; right < n; right++) {
    add(nums[right]);
    while (windowInvalid()) {
        remove(nums[left]);
        left++;
    }
}
```

- `right` moves from left to right once.
- `left` also moves from left to right once.
- Even though there is a nested `while`, total pointer movement is still `O(n)`.

This is a very common interview trap:

- nested loop does not always mean `O(n^2)`
- if each pointer only moves forward, total work can still be linear

---

## 13. O(1) Average for HashMap / HashSet Operations

```java
Map<Integer, Integer> map = new HashMap<>();
for (int num : nums) {
    map.put(num, map.getOrDefault(num, 0) + 1);
}
```

- `put`, `get`, and `containsKey` are usually `O(1)` average.
- If done `n` times, total is usually `O(n)`.

Important note:

- Strict worst case can degrade, but in algorithm interviews we usually use average-case `O(1)` for hash table operations.

---

## 14. O(log n) per Heap Operation

```java
PriorityQueue<Integer> heap = new PriorityQueue<>();
for (int num : nums) {
    heap.offer(num);
}
while (!heap.isEmpty()) {
    heap.poll();
}
```

- `offer()` is `O(log n)`
- `poll()` is `O(log n)`
- Doing one heap operation `n` times usually gives `O(n log n)`

Common patterns:

- top K
- merge K sorted lists
- running median

---

## 15. O(n) Recursion

```java
int sum(int n) {
    if (n == 0) {
        return 0;
    }
    return n + sum(n - 1);
}
```

- The function calls itself `n` times.
- Each level does `O(1)` extra work.
- Total time is `O(n)`.

---

## 16. O(log n) Recursion

```java
int f(int n) {
    if (n <= 1) {
        return 1;
    }
    return f(n / 2);
}
```

- Problem size is halved each call.
- Recursion depth is `O(log n)`.

---

## 17. O(n log n) Divide and Conquer

```java
void mergeSort(int[] nums, int left, int right) {
    if (left >= right) {
        return;
    }
    int mid = left + (right - left) / 2;
    mergeSort(nums, left, mid);
    mergeSort(nums, mid + 1, right);
    merge(nums, left, mid, right);
}
```

- There are `O(log n)` levels of recursion.
- Each level does `O(n)` total merge work.
- Total time is `O(n log n)`.

---

## 18. How To Read Time Complexity Quickly

When you see Java code, ask these questions:

1. How many times does each loop run?
2. Does the loop variable increase by `1`, double, or shrink the search space by half?
3. If there are nested loops, are they truly independent?
4. In recursion, what is the branching factor?
5. In recursion, how deep does the call tree go?
6. Is each `HashMap` / `HashSet` / `PriorityQueue` operation really `O(1)` or `O(log n)`?

---

## 19. Common Mistakes

- A nested `while` inside a `for` loop is not automatically `O(n^2)`.
- `HashMap` operations are usually average `O(1)`, not guaranteed worst-case `O(1)`.
- `PriorityQueue` insertion and removal are not `O(1)`; they are `O(log n)`.
- Recursive code is not judged only by call depth; also count how many branches each call creates.
- `for (int i = 0; i < n; i *= 2)` is wrong when `i` starts at `0`; it never changes.

---

## 20. Quick Summary Table

| Java pattern | Time complexity |
|----------|----------|
| single loop over `n` | `O(n)` |
| two nested loops over `n` | `O(n^2)` |
| three nested loops over `n` | `O(n^3)` |
| binary search | `O(log n)` |
| loop + binary search | `O(n log n)` |
| two pointers moving forward | `O(n)` |
| traverse two arrays | `O(m + n)` |
| BFS / DFS | `O(V + E)` |
| subset recursion | `O(2^n)` |
| permutation recursion | `O(n!)` |
| heap push/pop `n` times | `O(n log n)` |
| merge sort | `O(n log n)` |

