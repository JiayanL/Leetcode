class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def canPartitionAtIndex(current_index, remaining_sum):
            nonlocal dp
            # base case
            if remaining_sum == 0:
                return 1
            
            # check that our index is still valid
            if len(nums) == 0 or current_index >= len(nums):
                return 0
            
            # check that I've done the work
            if dp[current_index][remaining_sum] == -1:
                
                # include the current_index
                if nums[current_index] <= remaining_sum:
                    if canPartitionAtIndex(current_index + 1, remaining_sum - nums[current_index]) == 1:
                        dp[current_index][remaining_sum] = 1
                        # cut short the next calculation
                        return 1
                
                # don't include the current index
                dp[current_index][remaining_sum] = canPartitionAtIndex(current_index + 1, remaining_sum)
            
            return dp[current_index][remaining_sum]
        
        # top down dynamic programming
        s = sum(nums)
        
        # check if even
        if s % 2 != 0:
            return False
        
        # memoization based on capacity and the current index
        # -1 default, 1 true, 0 false
        dp = [[-1 for _ in range(int(s/2) + 1)] for _ in range(len(nums))]
        
        return True if canPartitionAtIndex(0, int(s/2)) == 1 else False
        