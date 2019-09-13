class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda x: x[0]-x[1])
        res = 0
        for i in range(len(costs)): res += costs[i][1]
        n = len(costs)//2
        for i in range(n):
            res += costs[i][0]-costs[i][1]
        return res