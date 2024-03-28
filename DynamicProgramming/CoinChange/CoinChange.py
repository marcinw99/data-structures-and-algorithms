from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dp():
            return 0

        return dp()


def test1():
    print(Solution().coinChange([1, 2, 5], 11))  # 3


def test2():
    print(Solution().coinChange([2], 3))  # -1


def test3():
    print(Solution().coinChange([1], 0))  # 0


test1()
test2()
test3()
