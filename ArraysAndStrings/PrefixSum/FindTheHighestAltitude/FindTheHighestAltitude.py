from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        answer = 0

        for num in gain:
            current += num
            answer = max(answer, current)

        return answer


def test1():
    print(Solution().largestAltitude([-5, 1, 5, 0, -7]))  # 1


test1()
