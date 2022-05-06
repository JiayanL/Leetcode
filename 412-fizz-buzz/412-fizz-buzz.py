class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            answer = ""
            if i % 3 == 0:
                answer += "Fizz"
            if i % 5 == 0:
                answer += "Buzz"
            if answer == "":
                answer = str(i)
            result.append(answer)
        return result
            