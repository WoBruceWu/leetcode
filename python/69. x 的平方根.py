class Solution(object):
    def mySqrt(self, x):
        """ 找到一个数n，满足n^2 <= x, (n+1)^2 > x
        :type x: int
        :rtype: int
        """
        low, high = 0, x
        while low < high:
            mid = (low+high)//2
            if mid**2 == x: return mid
            if mid**2 > x:
                high = mid
            elif (mid+1)**2 < x:
                low = mid
            elif (mid+1)**2 > x:
                return mid
            else:
                return mid+1
        return low

sol = Solution()
print(sol.mySqrt(2))