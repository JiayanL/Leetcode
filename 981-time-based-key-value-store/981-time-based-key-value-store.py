class TimeMap:

    def __init__(self):
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dic[key]
        l, r = 0, len(arr) - 1
        # binary search for 
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                l = mid + 1
            elif arr[mid][0] > timestamp:
                r = mid - 1
        # if there are no elements equal to or less than, we'll keep decrementing r
        if l == 0:
            return ""
        # since we move mid up by 1, if we haven't hit timestamp, we'll probalby have moved up by 1
        return arr[l - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)