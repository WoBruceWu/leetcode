class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        max_sum = max_left = nums[0]

        for i in range(1, len(nums)):
            if max_left > 0:
                max_left += nums[i]
            else:
                max_left = nums[i]
            max_sum = max(max_sum, max_left)

        return max_sum

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))