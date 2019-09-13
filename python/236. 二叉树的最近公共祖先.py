# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or root == p or root == q: return root

        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)

        return root if left_res and right_res else left_res if left_res else right_res



t3 = TreeNode(3)
t5 = TreeNode(5)
t1 = TreeNode(1)
t6 = TreeNode(6)
t2 = TreeNode(2)
t0 = TreeNode(0)
t8 = TreeNode(8)
t7 = TreeNode(7)
t4 = TreeNode(4)

t3.left, t3.right = t5, t1
t5.left, t5.right = t6,t2
t1.left, t1.right = t0, t8
t2.left, t2.right = t7, t4

sol = Solution()
print(sol.lowestCommonAncestor(t3, t5, t1))