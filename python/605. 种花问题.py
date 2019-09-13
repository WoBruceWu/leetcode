class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            if n == 0: return True
            flag = True
            if i > 0 and flowerbed[i-1] == 1: flag = False
            if i < len(flowerbed)-1 and flowerbed[i+1] == 1: flag = False
            if flowerbed[i] == 0 and flag:
                flowerbed[i] = 1
                n -= 1
        return True if n == 0 else False