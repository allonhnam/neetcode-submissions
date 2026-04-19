class TimeMap:
    def __init__(self):
        # keyStore maps each key to a list of [value, timestamp] pairs
        self.keyStore = {}  # key: List[[value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Initialize list if key not seen before
        if key not in self.keyStore:
            self.keyStore[key] = []
        # Append the new [value, timestamp] to the list
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""  # Default result if no valid timestamp is found
        values = self.keyStore.get(key, [])  # Get the list of [val, timestamp] for the key

        # Binary search for the latest timestamp <= given timestamp
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]  # Valid candidate found, try to find later one
                l = m + 1
            else:
                r = m - 1

        return res  # Return the best match found
