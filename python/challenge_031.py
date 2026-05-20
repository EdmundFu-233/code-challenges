"""Challenge 031 — LRU Cache Implementation

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
"""


class ListNode:
    """Doubly linked list node."""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """LRU Cache with O(1) get and put operations."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        # Dummy head and tail for sentinel pattern
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode) -> None:
        """Remove a node from the doubly linked list."""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_front(self, node: ListNode) -> None:
        """Add a node right after the head (most recently used position)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """Return the value of the key if exists, otherwise -1."""
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """Update or insert the key-value pair."""
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)


def test():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    print("Challenge 031 (LRU Cache) all tests passed!")


if __name__ == "__main__":
    test()
