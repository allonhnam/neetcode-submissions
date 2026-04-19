from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # Initializes the LRU cache with a given capacity using OrderedDict
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        # Retrieves the value of the key if present, and marks it as recently used
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # Inserts or updates the key-value pair and evicts the least recently used if capacity is exceeded
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
