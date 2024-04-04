from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}

        for num in arr:
            frequency = occurrences.get(num, 0) + 1
            occurrences[num] = frequency

        seen_occurrences = set()
        for _, val in occurrences.items():
            if val in seen_occurrences:
                return False
            else:
                seen_occurrences.add(val)

        return True


def test1():
    print(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # True


def test2():
    print(Solution().uniqueOccurrences([1, 2]))  # False


def test3():
    print(Solution().uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))  # True


test1()
test2()
test3()
