class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # track window start and max length of 1s
        window_start = 0
        max_length = 0
        ones_in_window = 0
        
        for window_end in range(len(nums)):
            # track ones in window
            if nums[window_end] == 1:
                ones_in_window += 1
            
            # shrink the window as long as I have more than k 0s
            while (window_end - window_start + 1 - ones_in_window) > k:
                start_char = nums[window_start]
                if start_char == 1:
                    ones_in_window -= 1
                window_start += 1
            
            # track max
            max_length = max(max_length, window_end - window_start + 1)
        return max_length