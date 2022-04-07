class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if not stones:
            return 0
        # brute force solution
        stones.sort()
        print(stones)
        # sort array
        while len(stones) > 1:
            x = stones[-1]
            y = stones[-2]
            # smash stones
            if x == y:
                stones = stones[:-2]
                stones.append(0)
            else:
                stones = stones[:-2]
                stones.append(x-y)
            print(stones)
            stones.sort() 
        return stones[0]
        