from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res = ''
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(self.comparator))
        for num in nums:
            res += num
        if res[0] == '0': return '0'
        return res


    def comparator(self, x, y):
        if x + y < y + x: return 1
        elif x + y > y + x: return -1
        else: return 0
