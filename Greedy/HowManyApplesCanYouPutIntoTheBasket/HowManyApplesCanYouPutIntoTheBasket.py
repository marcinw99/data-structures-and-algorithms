from typing import List


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        sorted_apples = weight.copy()
        sorted_apples.sort()

        i = 0
        remaining_weight = 5000

        while i < len(sorted_apples):
            if sorted_apples[i] <= remaining_weight:
                remaining_weight -= sorted_apples[i]
                i += 1
            else:
                return i

        return i


def test1():
    print(Solution().maxNumberOfApples([100, 200, 150, 1000]))  # 4


def test2():
    print(Solution().maxNumberOfApples([900, 950, 800, 1000, 700, 800]))  # 5


test1()
test2()
