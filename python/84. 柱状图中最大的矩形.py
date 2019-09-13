class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights: return 0
        left_idx, min_idx = 0, 0
        max_area = heights[0]
        for i in range(1, len(heights)):
            h = min(heights[min_idx], heights[i])
            # if (i-left_idx+1)*
    

