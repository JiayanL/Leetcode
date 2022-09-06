class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_index, second_index = 0, 0
        intersections = []

        # while loop to step through both lists
        while first_index < len(firstList) and second_index < len(secondList):
            first_interval = firstList[first_index]
            second_interval = secondList[second_index]

            # check if there's an intersection (if the start is between the other intersection)
            if second_interval[0] <= first_interval[0] <= second_interval[1] or \
            first_interval[0] <= second_interval[0] <= first_interval[1]:
                start = max(first_interval[0], second_interval[0])
                end = min(first_interval[1], second_interval[1])
                # add the intersected interval (max of the start, min of the ends)
                intersections.append([start, end])

            # move to the next interval (the one with the earlier end)
            if first_interval[1] < second_interval[1]:
                first_index += 1
            else:
                second_index += 1

        return intersections