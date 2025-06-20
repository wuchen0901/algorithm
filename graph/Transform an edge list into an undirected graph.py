from collections import deque

edges = [
    [1, 2],
    [1, 3],
    [2, 4],
    [3, 5],
    [4, 5],
    [5, 6]
]

if __name__ == '__main__':
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)

    print(graph)
