class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) == 0: return 0
        if len(ratings) == 1: return 1
        cands = [1 for _ in range(len(ratings))]

        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i] and cands[i+1] <= cands[i]:
                cands[i+1] = cands[i]+1

        for i in range(1, len(ratings))[::-1]:
            if ratings[i-1] > ratings[i] and cands[i-1] <= cands[i]:
                cands[i-1] = cands[i]+1

        res = 0
        for i in range(len(cands)):
            res += cands[i]

        return res