# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        first_half_values = []
        while fast and fast.next:
            fast = fast.next.next
            first_half_values.append(slow.val)
            slow = slow.next

        is_even = fast is None
        if not is_even:
            slow = slow.next

        i = len(first_half_values) - 1
        while slow:
            if slow.val != first_half_values[i]:
                return False
            slow = slow.next
            i -= 1

        return True


def create_nodes(values):
    root = ListNode(values[0])
    prev = root
    for i in range(1, len(values)):
        prev.next = ListNode(values[i])
        prev = prev.next
    return root


def test1():
    print(Solution().isPalindrome(create_nodes([1, 2, 2, 1])))  # True


def test2():
    print(Solution().isPalindrome(create_nodes([1, 2])))  # False


def test3():
    print(Solution().isPalindrome(create_nodes([1, 2, 3, 2, 1])))  # True


def test4():
    print(Solution().isPalindrome(create_nodes([1])))  # False


test1()
test2()
test3()
test4()
