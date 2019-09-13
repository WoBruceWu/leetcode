class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MIN_VAL = -0xffffffff
        num1 = num2 = num3 = MIN_VAL
        for num in nums:
            if num >= num1:
                if num > num1:
                    num3 = num2
                    num2 = num1
                num1 = num
            elif num >= num2:
                if num > num2:
                    num3 = num2
                num2 = num
            elif num >= num3:
                num3 = num

        if num3 == MIN_VAL:
            num3 = num1

        return num3

sol = Solution()
print(sol.thirdMax([2,2,5]))