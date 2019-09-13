class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # f(n) = !f(n-1) or !f(n-2) or !f(n-3)
        dp = [-1 for _ in range(n+1)]
        return self.helper(n, dp)

    def helper(self, n, dp):
        if n <= 3:
            dp[n] = 1
            return True
        if dp[n] != -1:
            return True if dp[n] == 1 else False
        else:
            dp[n-1] = self.helper(n-1, dp)
            dp[n-2] = self.helper(n-2, dp)
            dp[n-3] = self.helper(n-3, dp)
            if dp[n-1] == 0 or dp[n-2] == 0 or dp[n-3] == 0:
                return True
            else: return False