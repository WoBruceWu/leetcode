class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cur_idx = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[cur_idx] = nums[idx]
                cur_idx += 1
        return cur_idx