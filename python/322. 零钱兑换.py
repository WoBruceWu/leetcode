class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 非递归写法
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                dp[j] = min(dp[j-coins[i]] + 1, dp[j])
        if dp[-1] < float('inf'):
            return dp[-1]
        else:
            return -1

    # res = -1
    # def coinChange(self, coins, amount):
    #     amount_coin = {}
    #
    #
    # def helper(self, amount_coin, coins, amount):
    #     min_coin_num = -1
    #     for i in range(len(coins)):
    #         if amount-coins[i] not in amount_coin:
    #             coin_num = self.helper(amount_coin, coins, amount-coins[i])
    #             amount_coin[amount-coins[i]] = coin_num
    #
    #         if coin_num > 0:

