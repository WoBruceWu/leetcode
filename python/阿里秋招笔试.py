# yuzhi = int(input())
# min_len = int(input())
# max_len = int(input())
# intentions_a = input().split(',')
# intentions_b = input().split(',')
#
#
#
#
# intentions_common = []
# for intention_a in intentions_a:
#     if intention_a in intentions_b: intentions_common.append(intention_a)
#


def combine(n, k):
    """
    给定一个数组[1,2,3...n]，求这n个数中取k的数的组合，作为k个数的下标
    """
    if n == k:
        return [list(range(1, n + 1))]
    if k == 1:
        return [[i] for i in range(1, n + 1)]
    return combine(n - 1, k) + [j + [n] for j in combine(n - 1, k - 1)]

def helper(n, k):
    idx_group = combine(n, k)
    for idx_group in combine():
        pass



def minDistance(word1, word2):

    dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
    for i in range(len(word1) + 1): dp[i][0] = i
    for j in range(len(word2) + 1): dp[0][j] = j
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    return dp[len(word1)][len(word2)]

print(minDistance([1,2], [3,4]))