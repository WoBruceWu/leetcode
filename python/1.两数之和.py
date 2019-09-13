class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_dic = {}
        for idx, num in enumerate(nums):
            if num not in sum_dic:
                sum_dic[target-num] = idx
            else:
                return [sum_dic[num],idx]
        return None