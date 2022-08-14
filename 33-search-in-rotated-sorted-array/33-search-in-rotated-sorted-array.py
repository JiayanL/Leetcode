class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        # less than or equal bc we default l to the left
        while l <= r:
            # avoids overflow
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            
            # INVARIANT: one half will always be sorted
            # check if left is sorted
            if nums[mid] >= nums[l]:
                # check if target is in the left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                # check if target is in the right half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                
        return -1