class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        
        # go to each number
        # append each number to subsets
        for num in nums:
            # take all elements in subsets currently
            copy = subsets.copy()
            
            # append current element to each element in subsets and add
            for subset in copy:
                subset_copy = subset.copy()
                subset_copy.append(num)
                subsets.append(subset_copy)
        return subsets