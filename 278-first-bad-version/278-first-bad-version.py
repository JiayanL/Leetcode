# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        
        while left <= right:
            mid = (left + right) // 2
            # this version is bad
            if isBadVersion(mid):
                # check if this is the first one
                if not isBadVersion(mid - 1):
                    return mid
                # otherwise, go earlier
                else:
                    right = mid - 1
            
            # otherwise: go later
            else:
                left = mid + 1
                