import collections
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s))]
        end_dict = collections.defaultdict(list)
        for word in wordDict: end_dict[word[-1]].append(wordDict)
        for i in range(len(s)):
            if s[i] in end_dict:
                for word in end_dict[s[i]]:
                    if s[]