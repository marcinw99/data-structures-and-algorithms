# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEndBasic(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes_count = 0

        front_sentinel = ListNode(0)
        front_sentinel.next = head

        dummy = front_sentinel
        while dummy:
            nodes_count += 1
            dummy = dummy.next

        target_node_to_omit = nodes_count - n

        count = 1
        prev = front_sentinel
        dummy = front_sentinel.next
        while dummy:
            if count == target_node_to_omit:
                prev.next = dummy.next
                break
            prev = dummy
            dummy = dummy.next
            count += 1

        return front_sentinel.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front_sentinel = ListNode(0)
        front_sentinel.next = head

        helper_count_node = front_sentinel
        node_before_deleted_node = front_sentinel

        for i in range(n + 1):
            helper_count_node = helper_count_node.next

        while helper_count_node:
            helper_count_node = helper_count_node.next
            node_before_deleted_node = node_before_deleted_node.next

        node_before_deleted_node.next = node_before_deleted_node.next.next

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
    print_nodes(Solution().removeNthFromEnd(create_nodes([1, 2, 3, 4, 5]), 2))  # 1 2 3 5


def test2():
    print_nodes(Solution().removeNthFromEnd(create_nodes([1]), 1))  # []


def test3():
    print_nodes(Solution().removeNthFromEnd(create_nodes([1, 2]), 1))  # 1


test1()
test2()
test3()
