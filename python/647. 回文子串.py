class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        res = len(s)
        dp = [[False if i != j else True for j in range(len(s))] for i in range(len(s))]

        for i in range(len(s)-1)[::-1]:
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j-1 == i:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j]: res += 1

        return res

sol = Solution()
print(sol.countSubstrings("aaaaa"))
