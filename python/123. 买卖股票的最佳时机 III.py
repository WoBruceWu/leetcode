class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        transaction = 2
        dp[k][i] = max(dp[k][i-1], dp[k-1][j-1]+prices[i]-prices[j]) j=1...i-2, i=2,3...
        dp = [[0 for _ in range(len(prices))] for _ in range(transaction+1)]
        for k in range(1, len(transaction)+1):
            for i in range():
