import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap implementation
        maxHeap = []
        
        for (x, y) in points:
            dist = -(x ** 2 + y ** 2)
            
            if len(maxHeap) == k:
                heapq.heappushpop(maxHeap, (dist, x, y))
            else:
                heapq.heappush(maxHeap, (dist, x, y))
            
        return [(x,y) for (dist, x, y) in maxHeap]