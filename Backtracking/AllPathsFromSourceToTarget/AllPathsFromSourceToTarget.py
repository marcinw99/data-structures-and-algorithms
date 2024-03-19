from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        answer = []

        def backtrack(current, i):
            if i == target:
                answer.append(current[:])
                return

            for j in graph[i]:
                current.append(j)
                backtrack(current, j)
                current.pop()

        backtrack([0], 0)
        return answer


def test1():
    print(Solution().allPathsSourceTarget([[1, 2], [3], [3], []]))  # [[0,1,3], [0,2,3]]


def test2():
    print(Solution().allPathsSourceTarget(
        [[4, 3, 1], [3, 2, 4], [3], [4], []]))  # [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]


test1()
test2()
