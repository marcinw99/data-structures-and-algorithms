# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0

        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        reversal_head = prev
        result = reversal_head.val
        reversal_head = reversal_head.next
        next_factor = 2

        while reversal_head:
            result += reversal_head.val * next_factor
            next_factor *= 2
            reversal_head = reversal_head.next

        return result


def create_nodes(values):
    if not values:
        return None
    root = ListNode(values[0])
    prev = root
    for i in range(1, len(values)):
        prev.next = ListNode(values[i])
        prev = prev.next
    return root


def test1():
    print(Solution().getDecimalValue(create_nodes([1, 0, 1])))  # 5


def test2():
    print(Solution().getDecimalValue(create_nodes([0])))  # 0


test1()
test2()
