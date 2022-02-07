class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums and initialize array
        nums = sorted(nums)
        result = []
        
        # loop through array
        for i in range(len(nums) - 2):
            # check to make sure the current one is not a duplicate as the previous one
            ## also keep a check for 0th element because that won't have a predecessor
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
        # initialize left and right pointers and move
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                curr_num = nums[i]
                left_num = nums[left]
                right_num = nums[right]
                total = curr_num + left_num + right_num
                # attach the sum if it equals
                if total == 0:
                    result.append([curr_num, left_num, right_num])
                    # move left and right pointers, while avoiding duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1 
                    right -= 1
                # increment left pointer if sum is less than 0
                elif total < 0:
                    left += 1

                # decrement right pointer if sum is greater than 0
                elif total > 0:
                    right -= 1
        return result
        
        