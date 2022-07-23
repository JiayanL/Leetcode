class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort the array and initialize the result array
        nums.sort()
        result = []

        # loop through all unique elements in the array
        for i in range(0, len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # for each unique element in the array, loop through 
            # all unique proceeding elements inthe array
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                self.search_quads(nums, i, j, target, result)
        # run my search algorithm on all elements
        return result
        
    def search_quads(self, nums, first, second, target, result):
        # initialize left and right pointers
        left = second + 1
        right = len(nums) - 1
        
        while left < right:
            quad = nums[first] + nums[second] + nums[left] + nums[right]
            # add together and check that I've reached my target
            if quad == target:
                result.append([nums[first], nums[second], nums[left], nums[right]])
            # if I'm smaller than my target, move the left pointer to the right until we hit a unique one
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left -1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            if quad < target:
                left += 1
                # while nums[left] == nums[left - 1]:
                #     left += 1
            # if I'm larger, move the right pointer left
            if quad > target:
                right -= 1
                # while nums[right] == nums[right + 1]:
                #     right -= 1
