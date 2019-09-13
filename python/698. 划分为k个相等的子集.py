class Solution(object):
    res = False
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        target = sum(nums)
        if target % k != 0:
            return False
        target = target // k
        sums = [0 for _ in range(k)]
        nums.sort()
        nums = nums[::-1]
        if nums[0] > target: return False
        self.helper(nums, target, 0, sums)
        return self.res

    def helper(self, nums, target, idx, sums):
        if self.res: return
        if idx == len(nums):
            self.res = True
            return

        for i in range(len(sums)):
            if sums[i] > target: return
            elif sums[i] + nums[idx] == target or (sums[i] + nums[idx] + nums[-1]) <= target:
                sums[i] += nums[idx]
                self.helper(nums, target, idx+1, sums)
                sums[i] -= nums[idx]

sol = Solution()
print(sol.canPartitionKSubsets([7628,
3147,
7137,
2578,
7742,
2746,
4264,
7704,
9532,
9679,
8963,
3223,
2133,
7792,
5911,
3979]
, 6))
