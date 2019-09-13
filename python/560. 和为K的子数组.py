class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import collections
        freq_dic = collections.defaultdict(int)
        sum = res = 0
        for num in nums:
            sum += num
            if sum == k: res += 1
            res += freq_dic[sum-k]
            freq_dic[sum] += 1

        return res

sol = Solution()
print(sol.subarraySum([1,0,1], 2))