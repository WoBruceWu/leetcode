# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        path, res = [], []
        self.helper(root, sum, 0, path, res)
        return res

    def helper(self, root, sum, cur, path, res):
        if root == None: return
        if root.left == None and root.right == None:
            if cur + root.val == sum:
                res.append(path+[root.val])
            return
        self.helper(root.left, sum, cur+root.val, path+[root.val], res)
        self.helper(root.right, sum, cur+root.val, path+[root.val], res)
