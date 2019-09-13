class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cur_idx = 1, 1
        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx-1]:
                nums[cur_idx] = nums[idx]
                cur_idx += 1

        return cur_idx

sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))