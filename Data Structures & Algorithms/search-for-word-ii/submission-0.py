class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.word_index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, word_index):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]
        current.end_of_word = True
        current.word_index = word_index

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        result = []

        for i, word in enumerate(words):
            trie.insert(word, i)

        rows = len(board)
        cols = len(board[0])

        def dfs(r,c, node):

            if not (0 <= r < rows and 0<= c < cols):
                return 
            
            char = board[r][c]

            if char == "#" or char not in node.children:
                return 
            
            node = node.children[char]

            if node.end_of_word:
                result.append(words[node.word_index])
                node.end_of_word = False
            
            board[r][c] = "#"

            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)

            board[r][c] = char


        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)

        return result








        