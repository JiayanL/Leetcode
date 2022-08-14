class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(candidates, target, [], result)
        return result
        
    def backtrack(self, candidates, remaining, path, result):
        # check cases
        if remaining < 0:
            # cut this short
            return
        if remaining == 0:
            result.append(path)
            return
        for i in range(len(candidates)):
            # make sure I don't use previous elements again
            self.backtrack(candidates[i:], remaining - candidates[i], path + [candidates[i]], result)