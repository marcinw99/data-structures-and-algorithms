from collections import defaultdict
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        visited.add(0)

        def dfs(node):
            count = 1
            for neighbour in graph[node]:
                if neighbour not in restricted and neighbour not in visited:
                    visited.add(neighbour)
                    count += dfs(neighbour)
            return count

        return dfs(0)

    def reachableNodesIterative(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        visited.add(0)

        count = 1
        stack = [0]

        while len(stack) > 0:
            node = stack.pop()
            for neighbour in graph[node]:
                if neighbour not in restricted and neighbour not in visited:
                    visited.add(neighbour)
                    count += 1
                    stack.append(neighbour)

        return count

    def reachableNodesBetter(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            if a not in restricted and b not in restricted:
                graph[a].append(b)
                graph[b].append(a)

        visited = set()
        visited.add(0)

        def dfs(node):
            count = 1
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    count += dfs(neighbour)
            return count

        return dfs(0)

    def reachableNodesIterativeBetter(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            if a not in restricted and b not in restricted:
                graph[a].append(b)
                graph[b].append(a)

        visited = set()
        visited.add(0)

        count = 1
        stack = [0]

        while len(stack) > 0:
            node = stack.pop()
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    count += 1
                    stack.append(neighbour)

        return count

    def reachableNodesWeirdNotWorking(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        connected = defaultdict(list)
        unallocated = defaultdict(list)

        for a, b in edges:
            if a not in restricted and b not in restricted:
                if a == 0 or b == 0 or len(connected[a]) > 0 or len(connected[b]) > 0:
                    connected[a].append(b)
                    connected[b].append(a)
                    if len(unallocated[a]) > 0 or len(unallocated[b]) > 0:
                        stack = []
                        if len(unallocated[a]) > 0:
                            stack.append(a)
                        else:
                            stack.append(b)
                        while len(stack) > 0:
                            node = stack.pop()
                            connected[node].extend(unallocated[node])
                            stack.extend(unallocated[node])

                else:
                    unallocated[a].append(b)
                    unallocated[b].append(a)

        return sum(1 for attr_list in connected.values() if len(attr_list) > 0) or 1

    def reachableNodesBest(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        restricted_set = set(restricted)

        for a, b in edges:
            if a not in restricted_set and b not in restricted_set:
                graph[a].append(b)
                graph[b].append(a)

        visited = set()
        visited.add(0)
        # could also mark restricted as visited to be more optimal

        stack = [0]

        while len(stack) > 0:
            node = stack.pop()
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

        return len(visited)


def test1():
    print(Solution().reachableNodesBest(7, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]))  # 4


def test2():
    print(Solution().reachableNodesBest(7, [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]], [4, 2, 1]))  # 3


def test3():
    print(Solution().reachableNodesBest(2, [[0, 1]], [1]))  # 1


def test4():
    print(Solution().reachableNodesBest(10,
                                        [[8, 2], [2, 5], [5, 0], [2, 7], [1, 7], [3, 8], [0, 4], [3, 9], [1, 6]],
                                        [9, 8, 4, 5, 3, 1]))  # 1


def test5():
    print(Solution().reachableNodesBest(4,
                                        [[2, 1], [1, 0], [0, 3]],
                                        [3, 2]))  # 2


test1()
test2()
test3()
test4()
test5()
