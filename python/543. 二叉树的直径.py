# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.res

    def helper(self, root):
        if root == None: return 0
        if root.left == None and root.right == None: return 1
        l_h = self.helper(root.left)
        r_h = self.helper(root.right)
        self.res = max(self.res, l_h+r_h)
        return max(l_h, r_h)+1
