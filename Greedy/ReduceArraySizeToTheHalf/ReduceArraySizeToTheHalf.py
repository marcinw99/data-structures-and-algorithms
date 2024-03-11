from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        occurrences = Counter(arr)
        sorted_nums = sorted(occurrences.values(), reverse=True)
        removed = 0
        i = 0

        while removed < len(arr) / 2:
            removed += sorted_nums[i]
            i += 1

        return i


def test1():
    print(Solution().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))  # 2


def test2():
    print(Solution().minSetSize([7, 7, 7, 7, 7, 7]))  # 1


test1()
test2()
