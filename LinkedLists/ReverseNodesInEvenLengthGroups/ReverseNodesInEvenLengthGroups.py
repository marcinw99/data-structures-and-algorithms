# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroupsWrong(self, head: Optional[ListNode]) -> Optional[ListNode]:
        segment_length = 1
        dummy = head

        last_natural_order_node = None
        while head and head.next:
            if segment_length % 2 == 0:
                current_reversal_head = head
                reversal_prev = None
                i = 0
                while current_reversal_head and i < segment_length:
                    i += 1
                    next_node = current_reversal_head.next
                    current_reversal_head.next = reversal_prev
                    reversal_prev = current_reversal_head
                    current_reversal_head = next_node
                last_natural_order_node.next = reversal_prev
                head.next = current_reversal_head
                head = head.next
            else:
                i = 0
                while head and i < segment_length:
                    i += 1
                    last_natural_order_node = head
                    head = head.next
            segment_length += 1

        return dummy


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
    print_nodes(
        Solution().reverseEvenLengthGroups(create_nodes([5, 2, 6, 3, 9, 1, 7, 3, 8, 4])))  # [5,6,2,3,9,1,4,8,3,7]


def test2():
    print_nodes(Solution().reverseEvenLengthGroups(create_nodes([1, 1, 0, 6])))  # [1,0,1,6]


def test3():
    print_nodes(Solution().reverseEvenLengthGroups(create_nodes([1, 1, 0, 6, 5])))  # [1,0,1,5,6]


test1()
test2()
test3()
