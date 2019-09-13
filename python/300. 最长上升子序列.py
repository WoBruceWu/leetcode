class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None: return None
        if nums == []: return 0
        dp = [1 for _ in range(len(nums))]
        max_len = 1
        for i in range(1, len(nums)):
            for j in range(i)[::-1]:
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
            max_len = max(max_len, dp[i])
        return max_len

sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))