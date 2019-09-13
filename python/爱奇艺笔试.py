
N = int(input())
regus = [int(ch) for ch in input().split(' ')]


class Solution():
    res = 0
    def permute(self, nums, regus):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return None
        path = []
        self.helper(nums, path, regus)
        return self.res

    def helper(self, nums, path, regus):
        if len(nums) == 0:
            self.res += 1
            return
        for i in range(len(nums)):
            if len(path) > 0:
                if (regus[len(path)-1] == 1 and path[-1] > nums[i]) or (regus[len(path)-1] == 0 and path[-1] < nums[i]):
                    self.helper(nums[:i] + nums[i + 1:], path + [nums[i]], regus)
            else:
                self.helper(nums[:i] + nums[i + 1:], path + [nums[i]], regus)

nums = [i for i in range(1, N+1)]

sol = Solution()
print(sol.permute(nums, regus)%(10**9+7))

