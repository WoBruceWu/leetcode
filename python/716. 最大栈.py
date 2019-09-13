class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append(x)
            self.stack.append(x)
        else:
            max_num = self.stack[-1]
            self.stack.append(x)
            self.stack.append(max(max_num, x))

    def pop(self):
        """
        :rtype: int
        """
        self.stack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-2]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def popMax(self):
        """
        :rtype: int
        """

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()