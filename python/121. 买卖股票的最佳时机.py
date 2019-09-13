class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices)== 1: return 0
        min_price = prices[0]
        res = 0

        for i in range(1, len(prices)):
            res = max(prices[i]-min_price,res)
            min_price = min(min_price, prices[i])

        return res