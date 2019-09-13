class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low <= high:
            if nums[low] == target: return low
            if nums[high] == target: return high
            mid = (low+high)//2
            if nums[mid] == target: return mid
            con1 = True if nums[low] < nums[mid] and nums[mid] > nums[high] else False
            con2 = True if nums[low] > nums[mid] and nums[mid] < nums[high] else False
            if con1:
                if target > nums[low] and target < nums[mid]:
                    low += 1
                    high = mid-1
                else:
                    low = mid + 1
            elif con2:
                if target > nums[mid] and target < nums[high]:
                    low = mid + 1
                    high -= 1
                else: high = mid - 1
            else:
                if target == nums[mid]: return mid
                elif target < nums[mid]: high = mid - 1
                else: low = mid + 1
        return -1