class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        path, res = '', []
        self.helper(n, n, path, res)
        return res

    def helper(self, l, r, path, res):
        if l < 0: return
        if l == 0 and r == 0:
            res.append(path)
            return
        if l > r: return
        self.helper(l, r-1, path+')', res)
        self.helper(l-1, r, path+'(', res)


sol = Solution()
print(sol.generateParenthesis(3))