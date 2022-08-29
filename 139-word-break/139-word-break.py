class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = defaultdict(TrieNode)
    def addWord(self, word):
        curr = self
        for c in word:
            curr = curr.children[c]           
        curr.isWord = True
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # top down initialization
        n = len(s)
        # memoization, n + 1 for base case (first word we see)
        dp = [False] * (n + 1)
        dp[n] = True
        root = TrieNode()
        
        # create trie
        for word in wordDict:
            root.addWord(word)
        
        # DP -> find word
        for i in range(n-1, -1, -1):
            curr = root
            # from the current letter to the last letter
            for j in range(i+1, n+1):
                # check if this is in the word
                c = s[j-1]
                if c not in curr.children: break
                else:
                    curr = curr.children[c]
                # check if I've reached a new word
                if curr.isWord and dp[j]:
                    dp[i] = True
        return dp[0]