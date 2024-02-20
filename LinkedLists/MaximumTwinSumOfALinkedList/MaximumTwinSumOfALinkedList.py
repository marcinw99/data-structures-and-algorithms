class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def maximumTwinSumOfALinkedList(head: ListNode) -> int:
    fast = slow = head

    while fast and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    # reverse second half
    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        curr.next = prev
        prev = curr
        curr = next_node

    left_node = head
    right_node = prev
    answer = 0

    while left_node:
        sum = left_node.val + right_node.val
        if sum > answer:
            answer = sum
        left_node = left_node.next
        right_node = right_node.next

    return answer


node1 = ListNode(5)
node2 = ListNode(4)
node3 = ListNode(2)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4

print(maximumTwinSumOfALinkedList(node1))
