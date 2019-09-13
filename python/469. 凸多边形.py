class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) in [0, 1]: return False
        n = len(points)
        pre = 0
        for i in range(len(points)):
            dx1 = points[(i+1)%n][0]-points[i][0]
            dx2 = points[(i+2)%n][0]-points[i][0]
            dy1 = points[(i+1)%n][1]-points[i][1]
            dy2 = points[(i+2)%n][1]-points[i][1]

            cur = dx1*dy2-dx2*dy1
            if cur != 0:
                if pre * cur < 0: return False
                pre = cur
        return True
