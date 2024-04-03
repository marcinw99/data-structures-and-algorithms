from collections import defaultdict
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequencies = defaultdict(int)

        for num in arr:
            frequencies[num] += 1

        lucky_number = float("-inf")
        for num, frequency in frequencies.items():
            if num == frequency:
                lucky_number = max(lucky_number, num)

        return lucky_number if lucky_number != float("-inf") else -1


def test1():
    print(Solution().findLucky([2, 2, 3, 4]))  # 2


def test2():
    print(Solution().findLucky([1, 2, 2, 3, 3, 3]))  # 3


def test3():
    print(Solution().findLucky([2, 2, 2, 3, 3]))  # -1


test1()
test2()
test3()
