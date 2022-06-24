class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        result = []

        while i < len(firstList) and j < len(secondList):
            # check if a overlaps b
            a_overlaps_b = (firstList[i][0] >= secondList[j][0] and 
                            firstList[i][0] <= secondList[j][1])
            # check if b overlaps a
            b_overlaps_a = (secondList[j][0] >= firstList[i][0] and
                            secondList[j][0] <= firstList[i][1])

            # if overlap, insert overlapping interval
            if a_overlaps_b or b_overlaps_a:
                result.append([max(firstList[i][0], secondList[j][0]), 
                              min(firstList[i][1], secondList[j][1])])

            # move to the interval that finishes first
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result
    
    