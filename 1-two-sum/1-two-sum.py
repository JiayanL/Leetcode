class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}
        for i in range(len(nums)):
            curr = nums[i]
            if curr in difference:
                return [i, difference[curr]]
            difference[target - curr] = i