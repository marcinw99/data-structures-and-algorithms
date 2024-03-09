import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for coords in points:
            distance = coords[0] ** 2 + coords[1] ** 2  # alternative: math.dist([0, 0], coords)
            heapq.heappush(heap, (-distance, coords))
            if len(heap) > k:
                heapq.heappop(heap)

        return [obj[1] for obj in heap]


def test1():
    print(Solution().kClosest([[1, 3], [-2, 2]], 1))  # [[-2, 2]]


def test2():
    print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))  # [[3,3], [-2,4]]


test1()
test2()
