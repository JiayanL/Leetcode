class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_duplicate = 1
        
        for i in range(len(nums)):
            if nums[i] != nums[last_duplicate - 1]:
                nums[last_duplicate] = nums[i]
                last_duplicate += 1
                
        return last_duplicate