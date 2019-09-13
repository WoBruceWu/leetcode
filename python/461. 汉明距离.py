class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        for _ in range(32):
            x_bit, y_bit = x & 1, y & 1
            x >>= 1
            y >>= 1
            if x_bit != y_bit: res += 1

        return res

