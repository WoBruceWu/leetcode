class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        low = 0
        sum = 0
        min_len = 0xffffff
        for high, num in enumerate(nums):
            sum += num
            if sum >= s:
                while low <= high and sum >= s:
                    sum -= nums[low]
                    low += 1
                min_len = min(min_len, high-low+2)

        if min_len == 0xffffff: return 0
        return min_len

sol = Solution()
print(sol.minSubArrayLen(11,[1,2,3,4,5]))