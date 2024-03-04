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

        def dfs(start: int):
            for neighbour in graph[start]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    if neighbour == destination:
                        return True
                    elif dfs(neighbour):
                        return True

        return dfs(source) or False

    def validPathIterative(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        visited.add(source)

        stack = [source]

        while len(stack) > 0:
            node = stack.pop()
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    if neighbour == destination:
                        return True
                    stack.append(neighbour)

        return False

    def validPathDFSBetter(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()

        def dfs(node: int):
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for neighbour in graph[node]:
                    if dfs(neighbour):
                        return True
            return False

        return dfs(source)


def test1():
    print(Solution().validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))  # True


def test2():
    print(Solution().validPath(5, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))  # False


def test3():
    print(
        Solution().validPath(10,
                             [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]],
                             5,
                             9))  # True


test1()
test2()
test3()
