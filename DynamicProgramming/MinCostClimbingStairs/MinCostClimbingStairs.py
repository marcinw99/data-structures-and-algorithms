from functools import cache
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(i):
            if i <= 1:
                return 0
            return min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])

        return dp(len(cost))


def test1():
    print(Solution().minCostClimbingStairs([10, 15, 20]))  # 15


def test2():
    print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6


test1()
test2()
