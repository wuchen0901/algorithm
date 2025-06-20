from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E', 'F'],
    'D': ['F'],
    'E': [],
    'F': []
}



if __name__ == '__main__':
    queue = deque()
    queue.append('A')
    visited = set()
    while queue:
        e = queue.popleft()
        print(e)
        for node in graph[e]:
            if node in visited:
                continue
            visited.add(node)
            queue.append(node)

