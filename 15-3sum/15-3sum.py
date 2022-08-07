class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        i = 0
        
        while i < len(nums) - 2:
            # set up two pointers method
            left = i + 1
            right = len(nums) -1
            while left < right:
                # check that they're equal
                target = nums[i] + nums[left] + nums[right]
                
                if target == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
                # move right down
                elif target > 0:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                # move left up
                elif target < 0:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
            # move i to the next unique item
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return triplets