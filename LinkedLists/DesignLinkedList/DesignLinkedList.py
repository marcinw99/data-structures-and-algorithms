class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.sentinel_head = ListNode()

    def print_all(self):
        current = self.sentinel_head.next
        while current:
            print(current.value)
            current = current.next

    def get(self, index: int) -> int:
        current = self.sentinel_head
        for _ in range(index + 1):
            if not current.next:
                return -1
            current = current.next
        return current.value

    def addAtHead(self, val: int) -> None:
        current_head = self.sentinel_head.next
        self.sentinel_head.next = ListNode(val, current_head)

    def addAtTail(self, val: int) -> None:
        current = self.sentinel_head
        while current.next:
            current = current.next
        current.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        before = self.sentinel_head
        for _ in range(index):
            if not before.next:
                return None
            before = before.next
        after = before.next
        before.next = ListNode(val, after)

    def deleteAtIndex(self, index: int) -> None:
        before = self.sentinel_head
        for _ in range(index):
            if not before.next:
                return None
            before = before.next
        if before.next and before.next.next:
            before.next = before.next.next
        else:
            before.next = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

def test1():
    linked_list = MyLinkedList()
    linked_list.addAtHead(1)
    linked_list.addAtTail(3)
    linked_list.addAtIndex(1, 2)
    assert linked_list.get(1) == 2
    linked_list.deleteAtIndex(1)
    linked_list.print_all()
    assert linked_list.get(1) == 3


test1()
