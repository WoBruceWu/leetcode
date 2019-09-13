# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = -0xffffffff
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.res

    def helper(self, root):
        if root == None: return -0xffffff
        left_val = self.helper(root.left)
        right_val = self.helper(root.right)
        self.res = max(self.res, root.val, root.val+left_val, root.val+right_val, root.val+left_val+right_val)
        return max(root.val, root.val+left_val, root.val+right_val)
