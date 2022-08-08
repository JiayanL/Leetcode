class Solution:
    def canFinish (self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create an adjacency list and visited
        prereqCount = [0 for _ in range(numCourses)]
        courseUnlocks = [[] for _ in range(numCourses)]
        queue = collections.deque()
        visitedCount = 0
        
        for prereq in prerequisites:
            a, b = prereq[0], prereq[1]
            prereqCount[b] += 1
            courseUnlocks[a].append(b)
        
        for course, prereqs in enumerate(prereqCount):
            if prereqs == 0:
                queue.append(course)
                
                
        # if I visit another item, then I have a cycle
        while queue:
            currCourse = queue.popleft()
            visitedCount += 1
            for course in courseUnlocks[currCourse]:
                prereqCount[course] -= 1
                if prereqCount[course] == 0:
                    queue.append(course)
        # if prereqCount:
        #     return False
            
        if visitedCount == numCourses:
            return True
        return False
    
        
        
        