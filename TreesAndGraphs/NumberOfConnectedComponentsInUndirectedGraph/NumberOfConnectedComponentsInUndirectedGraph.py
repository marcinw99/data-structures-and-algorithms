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


def test1():
    print(Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]))  # 2


def test2():
    print(Solution().countComponents(1, [[0, 1], [1, 2], [2, 3], [3, 4]]))  # 1


test1()
test2()
