class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) in [0, 1]: return 0
        res = 0

        for i in range(len(prices)-1):
            res += max(0, prices[i+1]-prices[i])

        return res