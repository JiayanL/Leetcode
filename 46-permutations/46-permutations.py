class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums, path):
            # condition to append
            if not nums:
                result.append(list(path))
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(nums[:i] + nums[i+1:], path)
                path.pop()
            
        result = []
        backtrack(nums, [])
        return result