class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {
            2 : ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        def backtrack(index, path):
            if len(path) == len(digits):
                # I've reached the end
                combinations.append("".join(path))
                return
        
            for letter in digit_to_letters[int(digits[index])]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        
        if len(digits) == 0:
            return []
        combinations = []
        backtrack(0, [])
        return combinations