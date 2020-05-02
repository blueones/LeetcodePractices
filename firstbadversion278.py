# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start<= end:
            mid = (start+end)//2
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        return start
class Solution1:
    def firstBadVersion(self, n):
        start = 1
        end = n + 1
        while start < end:
            mid = (start + end)//2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start