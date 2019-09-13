class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        nums.sort()
        self.helper(nums, path, res)
        return res


    def helper(self, nums, path, res):
        if len(nums) == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            self.helper(nums[:i]+nums[i+1:], path+[nums[i]], res)

sol = Solution()
print(sol.permuteUnique([1,1,2]))