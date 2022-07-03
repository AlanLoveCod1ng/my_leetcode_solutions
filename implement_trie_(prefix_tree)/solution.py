class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        self.root.add(word)

    def search(self, word: str) -> bool:
        return self.root.search(word)

    def startsWith(self, prefix: str) -> bool:
        return self.root.searchPrefix(prefix)

class Node:
    def __init__(self):
        self.nodes = []
        self.end = False
        self.invalid = True

    def add(self, word):
        if len(self.nodes) == 0:
            self.nodes = [Node() for i in range(26)]
        self.invalid = False
        if len(word) == 0:
            self.end = True
            return
        charIndex = ord(word[0]) - ord('a')
        self.nodes[charIndex].add(word[1:])

    def search(self, word):
        if self.end and len(word) == 0:
            return True
        if not self.end and len(word) == 0:
            return False
        for i in range(len(self.nodes)):
            currentNode = self.nodes[i]
            currentChar = chr(i + ord('a'))
            if not currentNode.invalid:
                if currentChar == word[0]:
                    return currentNode.search(word[1:])


    def searchPrefix(self, word):
        if len(word) == 0:
            return True
        for i in range(len(self.nodes)):
            currentNode = self.nodes[i]
            currentChar = chr(i + ord('a'))
            if not currentNode.invalid:
                if currentChar == word[0]:
                    return currentNode.searchPrefix(word[1:])
