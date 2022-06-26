class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        
        for i in nums:
            if i in duplicate:
                return True
            duplicate[i] = 1
        
        return False