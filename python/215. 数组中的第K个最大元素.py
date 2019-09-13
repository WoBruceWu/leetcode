class Solution(object):
    res = 0
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.helper(nums, len(nums)-k+1, 0, len(nums)-1)
        return self.res

    def helper(self, nums, k, low, high):
        pvt_pos = self.partion(nums, low, high)
        if pvt_pos - low + 1 == k:
            self.res = nums[pvt_pos]
            return
        elif pvt_pos - low + 1 > k:
            self.helper(nums, k, low, pvt_pos-1)
        else:
            self.helper(nums, k-pvt_pos+low-1, pvt_pos+1, high)


    def partion(self, nums, low, high):
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        return low

sol = Solution()
nums = [3,2,1,5,6,4]
print(sol.findKthLargest(nums, 2))
print(nums)