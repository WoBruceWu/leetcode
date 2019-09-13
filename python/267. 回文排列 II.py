class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        import collections
        s_dic = collections.defaultdict(int)
        for i in range(len(s)):
            s_dic[s[i]] += 1
        odd_pair = 0
        for ch in s_dic:
            if s_dic[ch] % 2 == 1: odd_pair += 1
        if odd_pair > 1: return []
        elif odd_pair == 1 and len(s) % 2 == 0: return []

        mid = ''
        s_array = []
        for ch in s_dic:
            s_array.extend([ch for _ in range(s_dic[ch] // 2)])
            if s_dic[ch] % 2 == 1: mid = ch

        path = []
        res = []
        final_res = []
        self.helper(s_array, path, res)
        for path in res:
            s = ''.join(path)
            final_res.append(s+mid+s[::-1])

        return final_res


    def helper(self, nums, path, res):
        if len(nums) == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            self.helper(nums[:i]+nums[i+1:], path+[nums[i]], res)

sol = Solution()
print(sol.generatePalindromes("aaccbb"))