class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, [], result)
        return result
        
    def backtrack(self, nums, path, result):
        if not nums:
            result.append(path)
            return
    
        
        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i+1:], path + [nums[i]], result)