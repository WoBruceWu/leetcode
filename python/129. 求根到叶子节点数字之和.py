# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = 0
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root, 0)
        return self.res

    def helper(self, root, val):
        if root == None: return
        val = val*10 + root.val
        if root.left == None and root.right == None:
            self.res += val
        self.helper(root.left, val)
        self.helper(root.right, val)