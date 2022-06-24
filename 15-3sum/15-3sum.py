class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort array
        nums.sort()
        result = []
        
        # loop through each element in the arary, skipping duplicates
        for i in range(len(nums) - 2):
            
            # fastforward duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            # for each element, initialize a left and a right pointer, skipping duplicates
            l, r = i + 1, len(nums) - 1
        
            while l < r:
                    
                # add up the three items
                three_sum = nums[l] + nums[r] + nums[i]

                # if greater than 0:
                # move the right pointer left, skipping duplicates
                # making sure there's no overlap
                if three_sum > 0:
                    r -= 1

                # if less than 0
                # move the left pointer right, skipping duplicates
                # making sure there's no overlap
                elif three_sum < 0:
                    l += 1
                    
                # if equal 0
                # add the triplet to my results, and 
                # the left pointer over one if possible
                elif three_sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    
                    # move to the end of duplicates
                    while l + 1 < r and nums[l] == nums[l + 1]:
                        l += 1
                    while r - 1 > l and nums[r] == nums[r - 1]:
                        r -= 1
                        
                    # adjust since every k can noly have one number
                    
                    l += 1
                    r -= 1
        return result
