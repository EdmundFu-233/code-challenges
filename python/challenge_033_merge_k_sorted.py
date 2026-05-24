"""
Challenge 033: Merge K Sorted Lists

Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Example:
    Input: [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]

Uses a min-heap (priority queue) for O(N log k) time complexity,
where N is total nodes and k is the number of lists.
"""

import heapq
from typing import List, Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next_node: "ListNode" = None):
        self.val = val
        self.next = next_node


def merge_k_lists_naive(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Naive approach: repeatedly find min head among all lists.
    Time: O(k * N), Space: O(1)
    """
    dummy = ListNode(0)
    curr = dummy

    # Filter out empty lists
    active = [l for l in lists if l]

    while active:
        # Find the list with smallest head
        min_idx = 0
        for i in range(1, len(active)):
            if active[i].val < active[min_idx].val:
                min_idx = i

        curr.next = active[min_idx]
        curr = curr.next

        # Advance the chosen list
        active[min_idx] = active[min_idx].next
        if not active[min_idx]:
            active.pop(min_idx)

    return dummy.next


def merge_k_lists_heap(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Optimal: use a min-heap to always get the smallest head.
    Time: O(N log k), Space: O(k) for the heap.
    """
    dummy = ListNode(0)
    curr = dummy

    # Min-heap stores (value, list_index, node)
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


# --- Test ---
def list_from_array(arr):
    """Convert list to linked list for testing."""
    dummy = ListNode(0)
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def list_to_array(head):
    """Convert linked list back to list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    # Test case
    lists = [
        list_from_array([1, 4, 5]),
        list_from_array([1, 3, 4]),
        list_from_array([2, 6]),
    ]

    result = merge_k_lists_heap(lists)
    print("Merged:", list_to_array(result))
    # Expected: [1, 1, 2, 3, 4, 4, 5, 6]

    # Edge case: empty lists
    assert merge_k_lists_heap([]) is None
    assert merge_k_lists_heap([None, None]) is None
    assert list_to_array(merge_k_lists_heap([list_from_array([1])])) == [1]

    # Performance comparison
    import time

    large_lists = [list_from_array(list(range(i * 10, i * 10 + 10))) for i in range(100)]

    start = time.perf_counter()
    merge_k_lists_heap(large_lists)
    heap_time = time.perf_counter() - start
    print(f"Heap method: {heap_time:.6f}s")

    print("All tests passed!")
