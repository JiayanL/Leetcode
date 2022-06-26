class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init
        n = len(nums)
        if n == 0: 
            return 1
        i, j = 0, n -1
        
        # modified binary search
        while i <= j:

            # binary search
            mid = i + (j - i) // 2
            print(mid)
            if nums[mid] == target: 
                return mid
            
            
            # check if left is sorted
            if nums[mid] >= nums[i]:
                # check if target is in left
                if target >= nums[i] and target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                # check if target is in right
                if target > nums[mid] and target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return -1