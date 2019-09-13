# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    sum = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root)
        return root

    def helper(self, root):
        if root == None: return
        self.helper(root.right)
        self.sum += root.val
        root.val = self.sum
        self.helper(root.left)

