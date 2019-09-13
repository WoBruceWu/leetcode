class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(numbers)-1
        while low < high:
            sum = numbers[low]+numbers[high]
            if sum == target:
                return [low, high]
            elif sum > target:
                high -= 1
            else:
                low += 1