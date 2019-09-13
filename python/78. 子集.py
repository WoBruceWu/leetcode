class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == None: return None
        nums.sort()
        res = []
        path = []
        self.helper(nums, 0, path, res)
        return res

    def helper(self, nums, idx, path, res):
        res.append(path)
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]: continue
            self.helper(nums, i+1, path+[nums[i]], res)


sol = Solution()
print(sol.subsets([1,2,3]))