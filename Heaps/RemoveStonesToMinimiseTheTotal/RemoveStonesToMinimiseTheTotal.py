import heapq
import math
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)

        for _ in range(k):
            biggest = heapq.heappop(heap)
            heapq.heappush(heap, math.floor(biggest / 2))  # could also use //

        return -sum(heap)


def test1():
    print(Solution().minStoneSum([5, 4, 9], 2))  # 12


def test2():
    print(Solution().minStoneSum([4, 3, 6, 7], 3))  # 12


test1()
test2()
