# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_segment = 1

        dummy = head
        prev = None
        while dummy:
            if current_segment % 2 == 0:
                reversed_tail = dummy

                reversal_prev = None
                current = dummy
                i = 0
                next_node = None
                while current and i < current_segment:
                    i += 1
                    next_node = current.next
                    current.next = reversal_prev
                    reversal_prev = current
                    current = next_node

                prev.next = reversal_prev
                reversed_tail.next = next_node
                dummy = reversed_tail
            else:
                for i in range(current_segment):
                    prev = dummy
                    dummy = dummy.next
                    if not dummy:
                        break
            current_segment += 1

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
    print_nodes(
        Solution().reverseEvenLengthGroups(create_nodes([5, 2, 6, 3, 9, 1, 7, 3, 8, 4])))  # [5,6,2,3,9,1,4,8,3,7]


def test2():
    print_nodes(Solution().reverseEvenLengthGroups(create_nodes([1, 1, 0, 6])))  # [1,0,1,6]


test1()
test2()
