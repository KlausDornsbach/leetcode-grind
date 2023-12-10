# tries are simple data structures to make searches for words and prefixes faster
# in this implementation, every search operation is O(1) time complexity and O(n)
# for insertions, where n is the size of the string. memory complexity is O(n) also
# for n words being stored in the hash set.
class Trie:

    def __init__(self):
        self.prefixes = set()
        self.words = set()
    

    def insert(self, word: str) -> None:
        curr = ""
        for c in word:
            curr += c
            self.prefixes.add(curr)
        
        self.words.add(word)
        

    def search(self, word: str) -> bool:
        if word in self.words: return True 
        return False


    def startsWith(self, prefix: str) -> bool:
        if prefix in self.prefixes: return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)