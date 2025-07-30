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
        if node.prev:
            node.prev.next = node.next
            self.head = node
        if node.next:
            node.next.prev = node.prev
        elif node.prev:
            self.tail = node.prev
        return node.value

    def put(self, key: int, value: int) -> None:
        # todo: if self.nodes.get(key): remove the old node from the linked list and dict
        if len(self.nodes) == self.capacity:
            self.tail.prev.next = None
            node = self.tail
            self.tail = self.tail.prev
            del self.nodes[node.key]
        else:
            node = Node()

            if self.head:
                self.head.prev = node
            else:
                self.head = node
                self.tail = node

        self.nodes[key] = node
        node.key = key
        node.value = value
        node.prev = None
