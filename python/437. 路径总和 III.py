# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.sub_path_sum(root, sum)
        return self.res

    def sub_path_sum(self, root, sum):
        if root == None: return
        self.helper(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)

    def helper(self, root, sum):
        if root == None: return
        if sum == root.val: self.res += 1
        self.helper(root.left, sum-root.val)
        self.helper(root.right, sum-root.val)
