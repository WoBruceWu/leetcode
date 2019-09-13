def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) <= 1: return 0
    transactions = 2
    dp = [[0 for _ in range(len(prices)+1)]for _ in range(transactions+1)]
    for k in range(transactions):
        tmpMax = dp[k][1] - prices[0]
        for i in range(1, len(prices)+1):
            dp[k+1][i] = max(dp[k+1][i-1], prices[i-1] + tmpMax)
            tmpMax = max(tmpMax, dp[k][i]-prices[i-1])
    return dp[transactions][len(prices)]

nums = [ch for ch in input().split(' ')]
flag = True
for ch in nums:
    if not ch.isdigit():
        flag = False
        break
if flag:
    nums = [int(ch) for ch in nums]
    print(maxProfit(nums))
else:
    print(0)