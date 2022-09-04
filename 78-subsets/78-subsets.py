class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.dfs_backtracking(subsets, nums, [], 0)
        return subsets
    
    def dfs_backtracking(self, result, nums, path, index):
        result.append(list(path))
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs_backtracking(result, nums, path, i + 1)
            path.pop()
        
        