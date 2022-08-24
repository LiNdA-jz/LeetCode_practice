# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # not work
        ver = np.linspace(1,n,n)
        left, right = 0, n
        while left <= right:
            pivot = left + (right - left) // 2
            if (isBadVersion(ver[pivot])):
                return pivot
            else:
                left = pivot + 1
        return -1

        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left