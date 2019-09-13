import math
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        d = math.floor(math.sqrt(k))
        if d*d == k:
            return math[d-1][d-1]
