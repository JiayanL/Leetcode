class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            
            # find the half that is sorted
            
            # check if left half is sorted
            if nums[l] <= nums[mid]:
                # check if the target is in the left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                # target is in right half
                else:
                    l = mid + 1
            # check if right half is sorted
            elif nums[r] >= nums[mid]:
                # check if target is in right half
                if nums[r] >= target > nums[mid]:
                    l = mid + 1
                # target is in left half
                else:
                    r = mid - 1
    
        return -1