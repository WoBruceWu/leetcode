from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.childs = defaultdict(TrieNode)

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = self.root
        for ch in word:
            if ch not in p.childs: p.childs[ch] = TrieNode()
            p = p.childs[ch]
        p.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for ch in word:
            if ch not in p.childs: return False
            p = p.childs[ch]
        return p.is_word


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for ch in prefix:
            if ch not in p.childs: return False
            p = p.childs[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)