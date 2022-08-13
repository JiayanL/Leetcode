class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        index, n = 0, len(nums)
        
        # cyclical sort
        while index < n:
            value = nums[index] - 1
            
            if nums[value] != nums[index]:
                nums[value], nums[index] = nums[index], nums[value]
            else:
                index += 1
            
        # traverse
        for i in range(n):
            if nums[i] - 1 != i:
                return [nums[i], i + 1]
        