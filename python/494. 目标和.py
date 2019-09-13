import collections
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = [collections.defaultdict(int) for _ in range(len(nums))]
        return self.helper(nums, 0, S, dp)

    def helper(self, nums, idx, S, dp):
        if idx == len(nums)-1:
            if nums[idx] == S and nums[idx] == 0:
                dp[idx][S] = 2
            elif nums[idx] == S or nums[idx] == -S:
                dp[idx][S] = 1
            else:
                dp[idx][S] = 0
            return dp[idx][S]
        if S in dp[idx]: return dp[idx][S]
        res = self.helper(nums, idx+1, S+nums[idx], dp) + self.helper(nums, idx+1,  S-nums[idx], dp)
        dp[idx][S] = res
        return res

sol = Solution()
print(sol.findTargetSumWays([0,1]
, 1))