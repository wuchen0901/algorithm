from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        graph = defaultdict(list)
        for word in wordList:
            for i, c in enumerate(word):
                pattern = word[:i] + '*' + word[i + 1:]
                graph[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            word, steps = queue.popleft()
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                for neighbor in graph[pattern]:
                    if neighbor == endWord:
                        return steps + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))
        else:
            return 0
