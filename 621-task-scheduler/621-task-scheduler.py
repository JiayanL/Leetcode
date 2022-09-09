class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        General approach
        1. Find the most frequent element
        2. While we have the most frequent element, put it in
        3. Then put every other element in
        4. Use a heap to keep track of our elements and our frequency
        '''
        
        task_counter = collections.Counter(tasks)
        heap = []
        schedule_counter = 0
        
        # sort items by frequency
        for task, freq in task_counter.items():
            # insert negative so that it becomes a maxheap instead of minheap
            heapq.heappush(heap, (-freq, task))
        
        while heap:
            i, temp_heap = 0, []
            while i <= n:
                schedule_counter += 1
                
                # retrieve current task
                if heap:
                    freq, task = heapq.heappop(heap)
                    
                    if freq != -1:
                        temp_heap.append((freq, task))
                
                # check that I haven't exhausted everything
                if not heap and not temp_heap:
                    break
                else:
                    i += 1
            # add everything back
            for item in temp_heap:
                heapq.heappush(heap, (item[0] + 1, item[1]))
        return schedule_counter
        