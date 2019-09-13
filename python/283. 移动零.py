class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_num = 0
        for i in range(nums):
            if nums[i] != 0:
                nums[i-zero_num] = nums[i]
            else:
                zero_num += 1
        for i in range(1, zero_num+1):
            nums[-i] = 0




sol = Solution
