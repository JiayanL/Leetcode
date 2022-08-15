class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # insight -> still 2 pointers (Floyd's Cycle detection)
        # move slow and fast pointers until
        # 1. I've made an invalid move
        # 1a. I've moved in the opposite direction
        # 1b. I have a one element cycle
        # 2. I've caught up
        
        # return -1 if its invalid
        for i in range(len(nums)):
            is_forward = nums[i] >= 0
            slow, fast = i, i
            
            # move slow and fast
            while True:
                slow = self.nextIndex(nums, slow, is_forward)
                fast = self.nextIndex(nums, fast, is_forward)
                if fast != - 1:
                    fast = self.nextIndex(nums, fast, is_forward)

                # check for break cases
                if slow == -1 or fast == -1 or slow == fast:
                    break
            if slow != -1 and slow == fast:
                print(slow)
                return True
        return False
        
    def nextIndex(self, nums, index, is_forward):
        # check for invalid direction
        direction = nums[index] >= 0
        
        if is_forward != direction:
            return -1
        
        next_index = (index + nums[index]) % len(nums)
        
        # check that I've landed on the same one
        if next_index == index:
            next_index = -1
        
        return next_index