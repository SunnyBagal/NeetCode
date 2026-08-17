from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]

        curr.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Build Trie
        trie = Trie()

        for word in words:
            trie.addWord(word)

        root = trie.root

        ROWS, COLS = len(board), len(board[0])

        res = set()
        visit = set()

        def dfs(r, c, node, word):

            # Invalid position / already visited / character not in Trie
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or board[r][c] not in node.children
            ):
                return

            visit.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]

            # Found a complete word
            if node.isEnd:
                res.add(word)

            # Explore neighbors
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Backtrack
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)