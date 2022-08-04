class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        length = len(nums) / 2
        for key, value in count.items():
            if value > length:
                return key