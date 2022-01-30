from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table = {}
        self.usage = deque()
        
    def get(self, key: int) -> int:
        if key not in self.hash_table:
            return -1
        if key in self.usage:
            self.usage.remove(key)
        self.usage.append(key)
        return self.hash_table[key]

    def put(self, key: int, value: int) -> None:
        if len(self.hash_table.keys()) == self.capacity and key not in self.hash_table.keys():
            lrk = self.usage.popleft()
            self.hash_table.pop(lrk)
            # print(f'true: key: {key}, lrk: {lrk}, hash_table: {self.hash_table}\n')
        self.hash_table[key] = value
        if key in self.usage:
            self.usage.remove(key)
        self.usage.append(key)
        # print(f'___display___\n queue: {self.usage}\n table: {self.hash_table}\n')

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)