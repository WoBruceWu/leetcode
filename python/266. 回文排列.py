class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import collections
        s_dic = collections.defaultdict(int)
        for i in range(len(s)):
            s_dic[s[i]] += 1
        odd_pair = 0
        for ch in s_dic:
            if s_dic[ch] % 2 == 1: odd_pair += 1
        if odd_pair > 1: return False
        elif odd_pair == 1 and len(s) % 2 == 0: return False

        return True