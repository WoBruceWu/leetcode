class Solution(object):
    # def canPartition(self, nums):
    #     """ 二维dp记录方式
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     target = sum(nums)
    #     if target % 2 == 1:
    #         return False
    #     target //= 2
    #     dp = [[False for _ in range(target+1)] for _ in range(len(nums))]
    #
    #     for i in range(target+1):
    #         if nums[0] == i:
    #             dp[0][i] = True
    #
    #     for i in range(1, len(nums)):
    #         for j in range(target+1):
    #             if nums[i] <= j:
    #                 dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
    #             else:
    #                 dp[i][j] = dp[i-1][j]
    #
    #     return dp[-1][-1]

    def canPartition(self, nums):
        """ 一维dp记录方式
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2

        dp = [False for _ in range(target+1)]

        if nums[0] <= target:
            dp[nums[0]] = True

        for i in range(1, len(nums)):
            num = nums[i]
            for j in range(num, target+1)[::-1]:
                dp[j] = dp[j] or dp[j-num]

        return dp[target]

sol = Solution()
print(sol.canPartition([1, 2, 5]))
