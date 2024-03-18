import math
from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check(minimum_threshold):
            pieces_count = 0
            current_sweetness = 0

            for chunk in sweetness:
                current_sweetness += chunk
                if current_sweetness >= minimum_threshold:
                    pieces_count += 1
                    current_sweetness = 0

            return pieces_count >= k + 1

        left = min(sweetness)
        right = max(sweetness) * math.ceil(len(sweetness) / (k + 1))

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right


def test1():
    print(Solution().maximizeSweetness([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))  # 6


def test2():
    print(Solution().maximizeSweetness([5, 6, 7, 8, 9, 1, 2, 3, 4], 8))  # 1


def test3():
    print(Solution().maximizeSweetness([1, 2, 2, 1, 2, 2, 1, 2, 2], 2))  # 5


test1()
test2()
test3()
