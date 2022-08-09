from heapq import *

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        minRooms = 0
        minHeap = []
        
        # append the end time of the first meeting
        heappush(minHeap, intervals[0][1])
        
        for meeting in intervals[1:]:
            # clear out all rooms before
            if minHeap[0] <= meeting[0]:
                heappushpop(minHeap, meeting[1])
            else:
                heappush(minHeap, meeting[1])
        return len(minHeap)