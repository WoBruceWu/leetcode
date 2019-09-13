class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = nums.sorted()
        low, high = 0, len(nums)-1
        while low < len(nums) and nums[low] == sort_nums[low]:
            low += 1
        while high >= 0 and nums[high] == sort_nums[high]:
            high -= 1
        if low <= high: return high - low +1
        return 0