from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = head
    current = lastNodeBeforeReverse = dummy
    position = 1

    while position < left:
        lastNodeBeforeReverse = current
        current = current.next
        position += 1

    lastReversedNode = current
    prev = None
    while current and position <= right:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        position += 1

    lastNodeBeforeReverse.next = prev
    lastReversedNode.next = current

    return prev if left == 1 else dummy

def printListValues(head: ListNode):
    current = head
    while current:
        print(current.val)
        current = current.next

def baseTestCase():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    printListValues(reverseBetween(node1, 2, 4))

def anotherTestCase():
    node1 = ListNode(3)
    node2 = ListNode(5)
    node1.next = node2
    printListValues(reverseBetween(node1, 1, 2))

anotherTestCase()