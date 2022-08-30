class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        index, length = 0, len(nums)
        
        while index < length:
            # where this should be
            target_index = nums[index] - 1
            
            # check if this is 1. valid and 2. in the right position
            if 0 <= target_index < length and nums[target_index] != nums[index]:
                nums[target_index], nums[index] = nums[index], nums[target_index]
            else:
                index += 1

        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
    
        # otherwise, its the last number
        return length + 1