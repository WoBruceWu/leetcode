# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return None
        p = root
        stack = []
        res = []
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                res.append(node.val)
                p = node.right

        return res