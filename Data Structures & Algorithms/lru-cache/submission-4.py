from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}
        self.q = deque()

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        self.q.remove(key)
        self.q.append(key)
        return self.hmap[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.q.remove(key)
        elif len(self.q) == self.capacity:
            oldest = self.q.popleft()
            del self.hmap[oldest]
        self.q.append(key)
        self.hmap[key] = value

