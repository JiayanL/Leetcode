class Solution:
    def __init__(self):
        self.memo = []
        
    def climbStairs(self, n: int) -> int:
        self.memo = [0] * (n + 1)
        self.memo[1] = 1
        if n > 1:
            self.memo[2] = 2
        return self.recursiveClimb(n)
    
    def recursiveClimb(self, n: int) -> int:
        if not self.memo[n]:
            self.memo[n] = self.recursiveClimb(n-1) + self.recursiveClimb(n-2)
        return self.memo[n]
        