import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        answer = 0

        heap = sticks.copy()
        heapq.heapify(heap)

        while len(heap) > 1:
            smallest = heapq.heappop(heap)
            smallest_second = heapq.heappop(heap)

            new_stick = smallest + smallest_second

            answer += new_stick

            heapq.heappush(heap, new_stick)

        return answer


def test1():
    print(Solution().connectSticks([2, 4, 3]))  # 14


def test2():
    print(Solution().connectSticks([1, 8, 3, 5]))  # 30


def test3():
    print(Solution().connectSticks([5]))  # 0


test1()
test2()
test3()
