from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        visited.add(source)
        found = False

        def dfs(start: int):
            nonlocal found
            for neighbour in graph[start]:
                # if found:
                #     return True
                if neighbour not in visited:
                    visited.add(neighbour)
                    if neighbour == destination:
                        found = True
                    else:
                        dfs(neighbour)

        dfs(source)

        return found

    def validPathBetter(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        return True


def test1():
    print(Solution().validPathBetter(3, [[0, 1], [1, 2], [2, 0]], 0, 2))  # True


def test2():
    print(Solution().validPathBetter(5, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))  # False


def test3():
    print(
        Solution().validPathBetter(10, [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]],
                                   5,
                                   9))  # True


# test1()
# test2()
test3()
