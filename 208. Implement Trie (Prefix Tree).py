class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        self._insert_recursive(self.root, word)

    def _insert_recursive(self, node: TrieNode, suffix: str):
        if suffix == '':
            node.is_end = True
            return

        char = suffix[0]
        if char not in node.children:
            node.children[char] = TrieNode()
        self._insert_recursive(node.children[char], suffix[1:])

    def search(self, word: str) -> bool:
        return self._search_recursive(self.root, word)

    def _search_recursive(self, node: TrieNode, suffix: str) -> bool:
        if suffix == '':
            return node.is_end

        char = suffix[0]
        if char in node.children:
            return self._search_recursive(node.children[char], suffix[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        return self._starts_with_recursive(self.root, prefix)

    def _starts_with_recursive(self, node: TrieNode, suffix: str) -> bool:
        if suffix == '':
            return True

        char = suffix[0]
        if char in node.children:
            return self._starts_with_recursive(node.children[char], suffix[1:])
        else:
            return False