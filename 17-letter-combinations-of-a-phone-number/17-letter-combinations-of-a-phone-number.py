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
        if len(digits) == 0:
            return []
        results = self.processDigits([""], digit_to_letters, digits)
        return results
        
    def processDigits(self, results, digit_to_letters, digits: str) -> None:
        if len(digits) == 0:
            return results
        
        nextDigit = []
        for current_combination in results:
            for char in digit_to_letters[int(digits[0])]:
                new_combination = current_combination + char
                nextDigit.append(new_combination)
        results = nextDigit
        
        return self.processDigits(results, digit_to_letters, digits[1:])