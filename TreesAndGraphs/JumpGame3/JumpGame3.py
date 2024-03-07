from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visited = {start}

        while queue:
            i = queue.popleft()
            value = arr[i]

            if value == 0:
                return True

            if value <= i and i - value not in visited:
                visited.add(i - value)
                queue.append(i - value)

            if i + value < len(arr) and i + value not in visited:
                visited.add(i + value)
                queue.append(i + value)

        return False


def test1():
    print(Solution().canReach([4, 2, 3, 0, 3, 1, 2], 5))  # True


def test2():
    print(Solution().canReach([4, 2, 3, 0, 3, 1, 2], 0))  # True


def test3():
    print(Solution().canReach([3, 0, 2, 1, 2], 2))  # False


test1()
test2()
test3()
