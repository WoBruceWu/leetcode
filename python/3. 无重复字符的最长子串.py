class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_idx = {}
        max_len = 0
        start = 0
        for idx, ch in enumerate(s):
            if ch in char_idx and char_idx[ch] >= start:
                start = char_idx[ch]+1
            char_idx[ch] = idx
            max_len = max(max_len, idx-start+1)

        return max_len

sol = Solution()
print(sol.lengthOfLongestSubstring("aabaab!bb"))