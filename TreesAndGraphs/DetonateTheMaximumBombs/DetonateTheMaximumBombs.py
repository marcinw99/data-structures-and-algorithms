import math
from collections import defaultdict
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue

                main = bombs[i]
                second = bombs[j]
                if math.dist(main[:-1], second[:-1]) <= main[2]:
                    graph[i].append(j)

        answer = 0

        for i in range(len(bombs)):
            current = 0
            queue = [i]
            visited = {i}

            while queue:
                bomb = queue.pop()
                current += 1

                for in_vicinity_bomb in graph[bomb]:
                    if in_vicinity_bomb not in visited:
                        visited.add(in_vicinity_bomb)
                        queue.append(in_vicinity_bomb)

            answer = max(answer, current)

        return answer


def test1():
    print(Solution().maximumDetonation([[2, 1, 3], [6, 1, 4]]))  # 2


def test2():
    print(Solution().maximumDetonation([[1, 1, 5], [10, 10, 5]]))  # 1


def test3():
    print(Solution().maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))  # 5


def test4():
    print(Solution().maximumDetonation([[4, 4, 3], [4, 4, 3]]))  # 2


test1()
test2()
test3()
test4()
