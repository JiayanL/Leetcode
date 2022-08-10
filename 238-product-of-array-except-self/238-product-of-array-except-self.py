class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        rightProduct = 1
        
        # initiatlize leftProduct
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        # multiply by moving right product
        for i in range(len(nums) - 2, -1, -1):
            rightProduct = rightProduct * nums[i + 1]
            ans[i] = ans[i] * rightProduct
            
        return ans