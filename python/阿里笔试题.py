import random
import collections
class Solution(object):
    def combine(self, n, k):
        """
        给定一个数组[1,2,3...n]，求这n个数中取k的数的组合，作为100个数的下标
        """
        if n == k:
            return [list(range(1, n+1))]
        if k == 1:
            return [[i] for i in range(1, n+1)]
        return self.combine(n-1, k) + [j + [n] for j in self.combine(n-1, k-1)]


    def sample_with_no_back(self, m, n):
        # 计算无放回的组合个数
        res_set = set() # 记录最后组合的结果
        # 随机生成m个1到m以内的正整数
        nums = [random.randint(1,m) for _ in range(m)]
        print(nums)
        # 取下标
        idx_group = self.combine(len(nums), n)
        # 遍历所有下标的组合
        for group in idx_group:
            sum = 0
            for idx in group:
                sum += nums[idx-1]
            if sum == 88:
                l = []
                for i in group:
                    l.append(nums[i-1])
                l.sort()
                res_set.add(tuple(l)) # 去重
        print(res_set)
        return len(res_set)

    def sample_with_back(self, m, n):
        # 计算有放回的组合个数
        # 随机生成m个1到m以内的正整数,包括m
        nums = [random.randint(1, m) for _ in range(m)]
        res_path = [[set() for _ in range(89)] for _ in range(m+1)] # res_path[i][j]表示有放回取i个数，和为j的组合,set内每个元素都是一个tuple，表示路径
        print(nums)
        dp = [[0 for _ in range(89)] for _ in range(m+1)] # dp[i][j]代表有放回取i个数，和为j的组合的个数,其中j<=88，此处未做去重
        # 初始化只有1个数的情况
        for i in range(len(nums)):
            if nums[i] <= 88:
                dp[1][nums[i]] = 1
                s = set()
                s.add(tuple([nums[i]]))
                res_path[1][nums[i]] = s
        # 动态规划
        for i in range(2, n+1):
            for j in range(1, 89):
                for num in nums:
                    if j + num <= 88 and dp[i-1][j] > 0:
                        t_set = set()
                        for group in res_path[i-1][j]:
                            print(group)
                            n_g = list(group)+[num]
                            n_g.sort()
                            t_set.add(tuple(n_g))
                        res_path[i][j+num] = t_set
                        dp[i][j+num] = len(t_set)
        print(res_path[n][88])
        return len(res_path[n][88])



sol = Solution()
# print(sol.sample_with_no_back(100, 2))
print(sol.sample_with_back(100, 3))