class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        
        for i in nums:
            if i in visited:
                return True
            visited[i] = 0
        return False