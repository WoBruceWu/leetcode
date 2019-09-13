# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = [i for i in range(n)]
        res = 0
        while stack:
            if len(stack) == 1:
                res = stack[0]
                break
            a = stack.pop()
            b = stack.pop()
            if knows(a,b) and knows(b, a):
                pass
            elif not knows(a, b) and knows(b, a):
                stack.append(a)
            elif knows(a, b) and not knows(b, a):
                stack.append(b)
            else:
                pass

        for i in range(n):
            if i != res:
                if knows(res, i) or not knows(i, res):
                    return -1
        return res


