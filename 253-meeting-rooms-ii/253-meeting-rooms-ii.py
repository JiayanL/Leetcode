from heapq import *

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        minRooms = 0
        minHeap = []
        for meeting in intervals:
            # clear out all rooms before
            while (len(minHeap) > 0) and meeting[0] >= minHeap[0]:
                heappop(minHeap)
            heappush(minHeap, meeting[1])
            minRooms = max(minRooms, len(minHeap))
        return minRooms