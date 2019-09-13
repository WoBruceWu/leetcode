class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0: return 0
        if len(points) == 1: return 1

        points.sort(key=lambda x:x[0])

        res = 1
        far = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > far:
                res += 1
                far = points[i][1]
            else:
                far = min(far, points[i][1])

        return res

sol = Solution()
print(sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))