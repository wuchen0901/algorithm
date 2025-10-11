import random


class RandomizedSet:

    def __init__(self):
        self.array = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.array.append(val)
        self.map[val] = len(self.array) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        index = self.map[val]
        last_element = self.array[-1]

        self.array[index] = last_element
        self.map[last_element] = index

        self.array.pop()
        del self.map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.array)
