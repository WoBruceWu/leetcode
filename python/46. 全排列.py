class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return None
        path = []
        res = []
        self.helper(nums, path, res)
        return res


    def helper(self, nums, path, res):
        if len(nums) == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            self.helper(nums[:i]+nums[i+1:], path+[nums[i]], res)

sol = Solution()
print(sol.permute([1,2,3]))