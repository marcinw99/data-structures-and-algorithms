# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        prev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        if prev:
            prev.next = slow.next
        else:
            dummy = slow.next

        return dummy


def create_nodes(values):
    root = ListNode(values[0])
    prev = root
    for i in range(1, len(values)):
        prev.next = ListNode(values[i])
        prev = prev.next
    return root


def print_nodes(root: ListNode):
    next_node = root
    result = []
    while next_node:
        result.append(next_node.val)
        next_node = next_node.next
    print(result)


def test1():
    result = Solution().deleteMiddle(create_nodes([1, 3, 4, 7, 1, 2, 6]))  # 1, 3, 4, 1, 2, 6
    print_nodes(result)


def test2():
    result = Solution().deleteMiddle(create_nodes([1, 2, 3, 4]))  # 1, 2, 4
    print_nodes(result)


def test3():
    result = Solution().deleteMiddle(create_nodes([2, 1]))  # 2
    print_nodes(result)


def test4():
    print_nodes(Solution().deleteMiddle(create_nodes([1])))  #
    print_nodes(Solution().deleteMiddle(create_nodes([1, 2])))  # 1
    print_nodes(Solution().deleteMiddle(create_nodes([1, 2, 3])))  # 1,3
    print_nodes(Solution().deleteMiddle(create_nodes([1, 2, 3, 4])))  # 1,2,4
    print_nodes(Solution().deleteMiddle(create_nodes([1, 2, 3, 4, 5])))  # 1,2,4,5


# test1()
# test2()
# test3()
test4()
