class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        i = 0
        
        for i in range(len(nums) - 2):
        
            # system to set up duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # set up two pointers method
            left = i + 1
            right = len(nums) -1
            while left < right:
                # check that they're equal
                target = nums[i] + nums[left] + nums[right]
                
                if target == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # remove duplicates
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left -= 1
                
                # move right down
                elif target > 0:
                    right -= 1
                
                # move left up
                elif target < 0:
                    left += 1
                
        return triplets