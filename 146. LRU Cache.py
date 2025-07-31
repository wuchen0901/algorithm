from typing import Optional


class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        node = self.nodes.get(key)
        if not node:
            return -1
        self._move_to_head(key)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.nodes.get(key):
            self._update(key, value)
        else:
            self._insert(key, value)

    def _move_to_head(self, key):
        node = self.nodes[key]

        if node == self.head:
            return  # already at head

        # Detach node
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            # This means node == tail
            self.tail = node.prev

        # Move to head
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def _insert(self, key, value):
        if not self.head and not self.tail:
            node = Node()
            node.key = key
            node.value = value
            self.nodes[key] = node
            self.head = node
            self.tail = node
            return

        if len(self.nodes) == self.capacity:
            node = self._remove_tail()
            if node is None:
                node = Node()
        else:
            node = Node()

        self.nodes[key] = node
        node.key = key
        node.value = value
        node.prev = None
        node.next = self.head

        if self.head:
            self.head.prev = node
        self.head = node

        if not self.tail:
            self.tail = node

    def _update(self, key, value):
        self.nodes[key].value = value
        self._move_to_head(key)

    def _remove_tail(self) -> Optional[Node]:
        if not self.tail:
            return None

        tail = self.tail
        del self.nodes[tail.key]

        if tail.prev:
            tail.prev.next = None
            self.tail = tail.prev
        else:
            # Removing the only node in the list
            self.head = None
            self.tail = None

        # Clean the node
        tail.key = None
        tail.value = None
        tail.prev = None
        tail.next = None

        return tail
