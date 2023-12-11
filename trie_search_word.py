class TrieNode():
    def __init__(self, end=False):
        self.children = dict()
        self.end = end


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.end = True
            

    def search(self, word: str) -> bool:
        def backTrackingDfs(word: str, node: TrieNode) -> bool:        
            if word == "":
                return node.end

            c = word[0]

            if c == '.':
                for c in node.children:
                    if backTrackingDfs(word[1:], node.children[c]):
                        return True
            elif c not in node.children:
                return False                
            else:
                return backTrackingDfs(word[1:], node.children[c])

        return backTrackingDfs(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)