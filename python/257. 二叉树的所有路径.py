# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None: return None
        path, res = '', []
        self.helper(root, path, res)
        return res

    def helper(self, root, path, res):
        if root == None: return
        if root.left == None and root.right == None:
            path += str(root.val)
            res.append(path)
            return
        self.helper(root.left, path+str(root.val)+'->', res)
        self.helper(root.right, path+str(root.val)+'->', res)
