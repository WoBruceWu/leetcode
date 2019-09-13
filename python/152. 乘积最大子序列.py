class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod = nums[0]
        max_left = min_left = nums[0]
        for i in range(1, len(nums)):
            # 必须要同时更新
            max_left, min_left = max(nums[i], max_left*nums[i], min_left*nums[i]), min(nums[i], max_left*nums[i], min_left*nums[i])
            max_prod = max(max_prod, max_left)
        return max_prod

sol = Solution()
print(sol.maxProduct([-4, -3, -2]))
