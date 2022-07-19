class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum, max_sum = 0, float("-inf")
        
        for i in nums:
            curr_sum += i
            max_sum = max(curr_sum, max_sum)
            if curr_sum < 0:
                curr_sum = max(0, i)
            
        return max_sum
    
        
    