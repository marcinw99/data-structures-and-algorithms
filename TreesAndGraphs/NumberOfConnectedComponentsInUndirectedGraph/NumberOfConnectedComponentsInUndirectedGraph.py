from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        answer = 0

        def dfs(node: int):
            if node not in seen:
                seen.add(node)
                for neighbour in graph[node]:
                    dfs(neighbour)

        for i in range(n):
            if i not in seen:
                answer += 1
                dfs(i)

        return answer

    def countComponentsIterative(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        answer = 0

        def dfs(node: int):
            nonlocal seen
            stack = [node]
            while len(stack) > 0:
                node = stack.pop()
                for neighbour in graph[node]:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        stack.append(neighbour)

        for i in range(n):
            if i not in seen:
                seen.add(i)
                answer += 1
                dfs(i)

        return answer


def test1():
    print(Solution().countComponentsIterative(5, [[0, 1], [1, 2], [3, 4]]))  # 2


def test2():
    print(Solution().countComponentsIterative(1, [[0, 1], [1, 2], [2, 3], [3, 4]]))  # 1


test1()
test2()
