class TimeMap:

    def __init__(self):
        self.storage = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []

        self.storage[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.storage.get(key, [])
        l = 0
        r = len(values) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res

# time: O(log(n))
# space: O(n)

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)