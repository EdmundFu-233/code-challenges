"""
Challenge 035: Word Ladder

Given two words (beginWord and endWord) and a dictionary wordList,
find the length of the shortest transformation sequence from beginWord
to endWord such that:

  1. Only one letter can be changed at a time.
  2. Each transformed word must exist in the word list.

Return 0 if no such sequence exists.

Approach: Bidirectional BFS
- Search from both beginWord and endWord simultaneously.
- When the two frontiers meet, the shortest path is found.
- This reduces the search space from O(b^d) to O(b^(d/2)).

Complexity: O(M²·N) where M = word length, N = word list size.
"""

from collections import defaultdict, deque
from typing import List


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """Return the length of the shortest word ladder, or 0 if impossible."""
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    # Precompute wildcard patterns: "h*t" → ["hot", "hit", ...]
    patterns: dict[str, list[str]] = defaultdict(list)
    for word in word_set:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i + 1:]
            patterns[pattern].append(word)

    # Bidirectional BFS
    begin_queue = deque([(begin_word, 1)])
    end_queue = deque([(end_word, 1)])
    begin_visited: dict[str, int] = {begin_word: 1}
    end_visited: dict[str, int] = {end_word: 1}

    def bfs_step(
        queue: deque,
        visited: dict[str, int],
        other_visited: dict[str, int],
    ) -> int:
        word, steps = queue.popleft()
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i + 1:]
            for neighbor in patterns.get(pattern, []):
                # Check if frontiers meet
                if neighbor in other_visited:
                    return steps + other_visited[neighbor]
                if neighbor not in visited:
                    visited[neighbor] = steps + 1
                    queue.append((neighbor, steps + 1))
        return 0

    while begin_queue and end_queue:
        # Always expand the smaller frontier first
        if len(begin_queue) <= len(end_queue):
            result = bfs_step(begin_queue, begin_visited, end_visited)
        else:
            result = bfs_step(end_queue, end_visited, begin_visited)
        if result > 0:
            return result

    return 0


# --- test cases ---
if __name__ == "__main__":
    tests = [
        # (beginWord, endWord, wordList, expected)
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
        ("a", "c", ["a", "b", "c"], 2),
        ("hot", "dog", ["hot", "dog", "dot"], 3),
        ("red", "tax", ["red", "ted", "tad", "tax"], 4),
        ("leet", "code", ["leet", "code"], 0),  # not adjacent
    ]

    for begin, end, word_list, expected in tests:
        result = ladder_length(begin, end, word_list)
        assert result == expected, (
            f"ladder_length({begin!r}, {end!r}, ...) = {result}, expected {expected}"
        )
        print(f"✅ {begin} → {end}: {result} steps")

    print("\nAll tests passed!")
