class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        prod = 1
        res = 0
        for right in range(len(nums)):
            prod *= nums[right]
            while left <= right and prod >= k:
                prod//=nums[left]
                left += 1
            res += (right-left+1)
        return res

sol = Solution()
print(sol.numSubarrayProductLessThanK([10,5,2,6], 100))