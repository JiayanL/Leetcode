class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals.sort(key = lambda x: x[0])
        currentInterval = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            # check for overlap
            if intervals[i][0] <= currentInterval[1]:
                currentInterval[1] = max(currentInterval[1], intervals[i][1])
            else:
                result.append(currentInterval)
                currentInterval = intervals[i]
        
        result.append(currentInterval)
        return result