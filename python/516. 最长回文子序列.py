class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        res = 1
        dp = [[0 if i != j else 1 for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)-1)[::-1]:
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][len(s)-1]