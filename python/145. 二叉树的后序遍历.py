# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return None
        stack, res = [], []
        p, mark_node = root, None
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack[-1]
                if node.right == mark_node:
                    res.append(node.val)
                    mark_node = node
                    stack.pop()
                else:
                    p = node.right
                    mark_node = None

        return res