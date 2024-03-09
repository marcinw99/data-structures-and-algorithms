import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums.copy()
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

def test1():
    obj = KthLargest(3, [4, 5, 8, 2])
    print(obj.add(3))  # 4
    print(obj.add(5))  # 5
    print(obj.add(10))  # 5
    print(obj.add(9))  # 8
    print(obj.add(4))  # 8


def test2():
    obj = KthLargest(1, [])
    print(obj.add(-3))  # -3
    print(obj.add(-2))  # -2
    print(obj.add(-4))  # -2
    print(obj.add(0))  # 0
    print(obj.add(4))  # 4


def test3():
    obj = KthLargest(2, [0])
    print(obj.add(-1))  # -1
    print(obj.add(1))  # 0
    print(obj.add(-2))  # 0
    print(obj.add(-4))  # 0
    print(obj.add(3))  # 1


test1()
test2()
test3()
