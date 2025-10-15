# 系统-工程-基础算法思维层级对照 (Bilingual)

> 三个层级从下到上递进：先夯实基础算法，再让算法落地工程，再面向整体系统做协同优化。  
> The layers progress upward: build algorithm fundamentals, anchor them in engineering practice, then optimize with system-wide collaboration.

## 🧮 基础算法思维 (Theoretical-level)

- 理解算法正确性与复杂度（时间 / 空间）  
  Understand algorithm correctness and complexity (time/space).
- 能实现经典算法：排序、查找、DFS、DP、贪心、回溯  
  Implement classic algorithms: sorting, searching, DFS, DP, greedy, backtracking.
- 分析最坏 / 平均 / 最优复杂度  
  Analyze worst, average, and best-case complexity.
- 掌握算法范式与模板：分治、滑窗、单调栈、并查集等  
  Master algorithm paradigms and templates: divide & conquer, sliding window, monotonic stack, union-find, etc.
- 案例：快速排序、Dijkstra、Knapsack、KMP、Tarjan  
  Examples: QuickSort, Dijkstra, Knapsack, KMP, Tarjan.

---

## 🧩 工程算法思维 (Engineering-level)

- 把算法“落地”成可维护、可调优、可测试的模块  
  Turn algorithms into maintainable, tunable, testable modules.
- 平衡复杂度、内存、并发、安全性、可读性  
  Balance complexity, memory, concurrency, security, and readability.
- 使用正确数据结构：队列、堆、树、哈希表、索引、缓存  
  Choose appropriate data structures: queues, heaps, trees, hash tables, indexes, caches.
- 处理边界条件与异常：空值、越界、溢出、并发冲突  
  Handle edge cases and exceptions: nulls, out-of-bounds, overflow, race conditions.
- 根据场景选择算法：在线算法、流式处理、增量计算  
  Match algorithms to scenarios: online algorithms, streaming, incremental computation.
- 案例：LRU Cache、负载均衡算法、并发队列、动态规划优化  
  Examples: LRU cache, load balancing algorithms, concurrent queues, optimized DP.

---

## ⚙️ 系统优化级算法思维 (System-level)

- 关注真实运行环境：CPU 缓存 / GC / IO / 并发 / 网络  
  Focus on real runtime environments: CPU cache, GC, IO, concurrency, networking.
- 根据数据分布选择策略：随机→线性；连续→二分/批处理  
  Tailor strategies to data distribution: random→linear; continuous→binary/ batched.
- 利用硬件：SIMD、cache locality、NUMA、并行管线  
  Leverage hardware: SIMD, cache locality, NUMA, parallel pipelines.
- 优化代价模型：降低延迟、提升吞吐、减少上下文切换  
  Optimize cost models: reduce latency, boost throughput, cut context switches.
- 面向火焰图思维：定位瓶颈、做 profiling 驱动优化  
  Think in flame graphs: locate bottlenecks, drive optimization via profiling.
- 全局最优而非局部最优，算法与系统协同  
  Seek global rather than local optima; align algorithms with system behavior.
- 案例：Timsort、Cuckoo Hash、MapReduce Sort、内存池化  
  Examples: Timsort, Cuckoo hash, MapReduce sort, memory pooling.
