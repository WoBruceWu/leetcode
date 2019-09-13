class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        swaped = False
        for i in range(1, len(nums))[::-1]:
            if nums[i] > nums[i-1]:
                nums[i:] = nums[i:][::-1]
                for j in range(i, len(nums)):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        break
                swaped = True
                break
        if not swaped:
            for i in range(len(nums)//2):
                nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]

sol = Solution()
nums = [1,1,1]
sol.nextPermutation(nums)
print(nums)