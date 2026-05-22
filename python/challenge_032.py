"""Challenge 032: Autocomplete System with Trie

Implement an autocomplete system using a Trie data structure.
Given a prefix, return all words that start with that prefix.
"""

from typing import List


class TrieNode:
    __slots__ = ("children", "is_end", "word")

    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None


class Autocomplete:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        node.word = word

    def _dfs(self, node: TrieNode, results: List[str]) -> None:
        if node.is_end:
            results.append(node.word)
        for child in node.children.values():
            self._dfs(child, results)

    def suggest(self, prefix: str) -> List[str]:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        results = []
        self._dfs(node, results)
        return sorted(results)


if __name__ == "__main__":
    ac = Autocomplete()
    for w in ["apple", "app", "application", "apt", "bat", "ball", "cat"]:
        ac.insert(w)
    print(ac.suggest("ap"))
    print(ac.suggest("ba"))
    print(ac.suggest("z"))
