import heapq

class MedianFinder:

    def __init__(self):
        # keeps track of 0....n/2
        self.max_heap = []
        # keep track of n/2....n
        self.min_heap = []
        self.length = 0
        
    def addNum(self, num: int) -> None:  
        # check whether num goes into max heap or min heap
        # num goes into max heap if its less than its largest element
        if self.max_heap:
            largest_in_max_heap = -self.max_heap[0]
            if num <= largest_in_max_heap:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
            
        # check if should be in minHeap
        if len(self.max_heap) > len(self.min_heap) + 1:
            curr = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, curr)
        if len(self.min_heap) > len(self.max_heap):
            curr = -1 * heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, curr)
        self.length += 1

    def findMedian(self) -> float:
        # case 1: even length
        if self.length % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        # case 2: odd length
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()