class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # bottom up
        # check if we can make a partition with the first i numbers
        s = sum(nums)
        
        # check if even
        if s % 2 != 0:
            return False
        
        # memoization based on sum and the current index
        # -1 default, 1 true, 0 false
        dp = [[False for _ in range(int(s/2) + 1)] for _ in range(len(nums))]
        
        # populate 0s
        for i in range(len(nums)):
            dp[i][0] = True
            
        # populate the first number
        for i in range(1, (int(s/2) + 1)):
            dp[0][i] = nums[0] == i
        
        # process all subsets for all sums
        for i in range(1, len(nums)):
            for j in range(1, int(s/2) + 1):
                # check if we've already made the partition (exclude)
                if dp[i - 1][j]:
                    dp[i][j] = dp[i-1][j]
                # check if we can get a partition by including
                # make sure that the sum is bigger than our current num
                elif j >= nums[i]:
                    # previous stage, previous capacity
                    dp[i][j] = dp[i-1][j-nums[i]]
        return dp[len(nums) - 1][int(s/2)]