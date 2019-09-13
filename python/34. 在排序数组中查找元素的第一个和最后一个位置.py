class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(nums)-1
        return self.helper(low, high, nums, target)

    def helper(self, low, high, nums, target):
        if low > high or low < 0 or high >= len(nums): return [-1, -1]
        mid = (low + high) // 2
        if target > nums[mid]:
            return self.helper(mid+1, high, nums, target)
        elif target == nums[mid]:
            l = r = mid
            [left, _] = self.helper(low, mid-1, nums, target)
            # print(mid+1, high, nums, target)
            [_, right] = self.helper(mid+1, high, nums, target)
            if left >= 0: l = left
            if right >= 0: r = right
            return [l, r]
        else:
            return self.helper(low, mid-1, nums, target)

sol = Solution()
print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))