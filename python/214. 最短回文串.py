class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)):
            low1, high1 = self.helper(s, i, i)
            low2, high2 = self.helper(s, i, i+1)

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)):
            low1, high1 = self.helper(s, i, i)
            low2, high2 = self.helper(s, i, i + 1)

    def helper(self, s, low, high):
        while low >= 0 and high <= len(s) - 1 and s[low] == s[high]:
            low -= 1
            high += 1
        return low, high


    def helper(self, s, low, high):
        while low >= 0 and high <= len(s)-1 and s[low] == s[high]:
            low -= 1
            high += 1
        return low, high