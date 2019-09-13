class Solution(object):
    # def trap(self, height):
    #     """
    #     o(n^2)时间复杂度，向两边找最大
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #     area = 0
    #     for i in range(1, len(height)-1):
    #         low, high = i-1, i+1
    #         for j in range(i-1)[::-1]:
    #             if height[j] > height[low]: low = j
    #         for j in range(i+1,len(height)):
    #             if height[j] > height[high]: high = j
    #         if height[low] > height[i] and height[high] > height[i]:
    #             area += (min(height[low], height[high])-height[i])
    #     return area

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0: return 0
        area = 0
        max_height = -1
        idx = 0
        for i in range(len(height)):
            if height[i] > max_height:
                max_height = height[i]
                idx = i

        max_left, max_right = height[0], height[-1]

        # 从左往右
        for i in range(1, idx):
            max_left = max(max_left, height[i])
            area += max(0, max_left-height[i])
        # 从右往左
        for i in range(idx+1, len(height)-1)[::-1]:
            max_right = max(max_right, height[i])
            area += max(0, max_right-height[i])

        return area




solu = Solution()
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# solu.trap(height)
height = [5,2,1,2,1,5]
print(solu.trap(height))





