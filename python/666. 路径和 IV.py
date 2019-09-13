class Solution(object):
    res = 0
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tree_dict = {}
        for num in nums:
            tree_dict[num//10] = num%10

        self.helper(tree_dict, 11, 0)
        return self.res

    def helper(self, tree_dict, root, val):
        if root not in tree_dict: return
        digit_h, digit_t = root//10, root%10
        left = (digit_h+1)*10 + digit_t*2-1
        right = (digit_h+1)*10 + digit_t*2
        if left not in tree_dict and right not in tree_dict:
            self.res += (val+tree_dict[root])
            return
        self.helper(tree_dict, left, tree_dict[root]+val)
        self.helper(tree_dict, right, tree_dict[root]+val)
