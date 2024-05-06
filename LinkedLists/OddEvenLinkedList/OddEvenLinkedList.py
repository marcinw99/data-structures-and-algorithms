# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = head
        even_chain_head = ListNode()
        even_chain_tail = even_chain_head
        odd_chain_tail = ListNode()
        is_even = False

        while head:
            if is_even:
                even_chain_tail.next = head
                even_chain_tail = even_chain_tail.next
            else:
                odd_chain_tail.next = head
                odd_chain_tail = odd_chain_tail.next
            head = head.next
            is_even = not is_even

        if is_even:
            even_chain_tail.next = None

        odd_chain_tail.next = even_chain_head.next

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
    print_nodes(Solution().oddEvenList(create_nodes([1, 2, 3, 4, 5])))  # [1,3,5,2,4]


def test2():
    print_nodes(Solution().oddEvenList(create_nodes([2, 1, 3, 5, 6, 4, 7])))  # [2,3,6,7,1,5,4]


test1()
test2()
