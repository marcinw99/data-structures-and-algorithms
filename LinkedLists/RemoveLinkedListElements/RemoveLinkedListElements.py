# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        front_sentinel = ListNode(val - 1)
        front_sentinel.next = head

        dummy = front_sentinel

        while dummy and dummy.next:
            if dummy.next.val == val:
                if dummy.next.next:
                    dummy.next = dummy.next.next
                else:
                    dummy.next = None
            else:
                dummy = dummy.next

        return front_sentinel.next


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
    print_nodes(Solution().removeElements(create_nodes([1, 2, 6, 3, 4, 5, 6]), 6))


def test2():
    print_nodes(Solution().removeElements(create_nodes([]), 1))


def test3():
    print_nodes(Solution().removeElements(create_nodes([7, 7, 7, 7]), 7))


test1()
test2()
test3()
