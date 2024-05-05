# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first_target_node = head
        second_target_node = head
        fast_pointer = head
        for _ in range(k-1):
            first_target_node = first_target_node.next

        for _ in range(k):
            fast_pointer = fast_pointer.next

        while fast_pointer:
            second_target_node = second_target_node.next
            fast_pointer = fast_pointer.next

        first_target_node.val, second_target_node.val = second_target_node.val, first_target_node.val

        return head


def create_nodes(values):
    if not values:
        return None
    root = ListNode(values[0])
    prev = root
    for i in range(1, len(values)):
        prev.next = ListNode(values[i])
        prev = prev.next
    return root


def print_nodes(root: ListNode):
    if not root:
        return
    next_node = root
    result = []
    while next_node:
        result.append(next_node.val)
        next_node = next_node.next
    print(result)


def test1():
    print_nodes(Solution().swapNodes(create_nodes([1, 2, 3, 4, 5]), 2))  # 1 4 3 2 5


def test2():
    print_nodes(Solution().swapNodes(create_nodes([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), 5))  # 7,9,6,6,8,7,3,0,9,5


test1()
test2()
