class Solution():
    def longestPalindrome(self, s):
        """ 动态规划法,使用转移方程的方式来理解
        :type s: str
        :rtype: str
        """
        dp = [[False if i != j else True for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)-1)[::-1]:
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
