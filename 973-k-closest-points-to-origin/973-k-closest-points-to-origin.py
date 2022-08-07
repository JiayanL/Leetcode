class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceAdjusted =[]
        # easiest way: calculate all distances, sort by distance, and return
        for coords in points:
            distanceAdjusted.append([self.calculateDistance(coords), coords[0], coords[1]])
        
        distanceAdjusted.sort(key=lambda x: x[0])
        result = distanceAdjusted[:k]
        result = list(map(lambda x: x[1:], result))
        return result
        # probably better: sort by distance in queue until full and return
    def calculateDistance(self, points):
        x, y = points[0], points[1]
        print(x, y)
        return math.sqrt(x ** 2 + y ** 2)