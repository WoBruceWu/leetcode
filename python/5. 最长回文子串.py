class Solution(object):
    # def longestPalindrome(self, s):
    #     """ 动态规划法,使用长度的方式来理解
    #     :type s: str
    #     :rtype: str
    #     """
    #     if len(s) == 0: return ''
    #     start = 0
    #     end = 1
    #     dp = [[False if i != j else True for i in range(len(s))] for j in range(len(s))] # 初始一字母的回文
    #     for i in range(len(s)-1):
    #         dp[i][i+1] = True if s[i] == s[i+1] else False # 初始二字母的回文
    #         if dp[i][i+1]: start, end = i, i+2
    #
    #     for l in range(3, len(s)+1): # 计算长度为3，4，5...的字母
    #         for i in range(len(s)-l+1):
    #             if s[i] == s[i+l-1]:
    #                 dp[i][i+l-1] = dp[i+1][i+l-2]
    #                 if dp[i][i+l-1]:
    #                     start, end = i, i+l
    #
    #     return s[start:end]


    def longestPalindrome(self, s):
        """ 动态规划法,使用转移方程的方式来理解
        :type s: str
        :rtype: str
        """
        if len(s) == 0: return ''
        start, end = 0, 0
        max_len = 1
        dp = [[True if i == j else False for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)-1)[::-1]:
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j-i+1 > max_len:
                    start, end, max_len = i, j, j-i+1
        return s[start:end+1]


    def longestPalindrome(self, s):
        """ 中心扩展法
        :type s: str
        :rtype: str
        """
        if len(s) == 0: return ''
        start = end = 0
        for i in range(len(s)):
            l1 = self.helper(s, i,i)
            l2 = self.helper(s, i, i+1)
            l = max(l1,l2)
            if l > end-start+1:
                start = i - (l-1)//2
                end = i + l//2

        return s[start:end+1]


    def helper(self, s, low, high):
        while low >= 0 and high < len(s) and s[low] == s[high]:
            low -= 1
            high += 1
        return high - low -1



sol = Solution()
print(sol.longestPalindrome('babad'))
