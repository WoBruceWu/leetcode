class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        prod = 1
        k -= 1
        for i in range(1, n+1): prod *= i
        nums = [str(i) for i in range(1, n+1)]
        for i in range(1, n):
            prod//=(n-i+1)
            group = k//prod
            res += nums[group]
            print(nums, group)
            nums = nums[:group] + nums[group+1:]
            k %= prod
        res += nums[0]
        return res

sol = Solution()
print(sol.getPermutation(4, 6))