class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_dic = {}
        sum = 0
        res = 0
        for idx, num in enumerate(nums):
            sum += num
            if sum == k:
                res = max(idx+1, res)
            if sum - k in num_dic:
                res = max(idx-num_dic[sum-k],res)
            if sum not in num_dic:
                num_dic[sum] = idx
        return res


sol = Solution()
print(sol.maxSubArrayLen([1,-1,5,-2,3], 3))