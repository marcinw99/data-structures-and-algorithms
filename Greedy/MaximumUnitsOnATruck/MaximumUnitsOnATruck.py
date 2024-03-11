from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted = boxTypes.copy()

        sorted.sort(key=lambda x: x[1])

        remaining_size = truckSize
        aggregated_units = 0

        while remaining_size > 0 and len(sorted):
            if sorted[-1][0] <= remaining_size:
                remaining_size -= sorted[-1][0]
                aggregated_units += sorted[-1][0] * sorted[-1][1]
                sorted.pop()
            else:
                aggregated_units += remaining_size * sorted[-1][1]
                sorted[-1][0] -= remaining_size
                remaining_size = 0

        return aggregated_units


def test1():
    print(Solution().maximumUnits([[1, 3], [2, 2], [3, 1]], 4))  # 8


def test2():
    print(Solution().maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10))  # 91


test1()
test2()
