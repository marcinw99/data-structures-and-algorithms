from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []

        def backtrack(current):
            current_sum = sum(current)

            if len(current) == k and current_sum == n:
                answer.append(current[:])
                return

            for i in range(current[-1], 10):
                if i in current:
                    continue
                if current_sum + i <= n:
                    current.append(i)
                    backtrack(current)
                    current.pop()

        for j in range(1, 10):
            if j < n:
                backtrack([j])

        return answer


def test1():
    print(Solution().combinationSum3(3, 7))  # [[1,2,4]]


def test2():
    print(Solution().combinationSum3(3, 9))  # [[1,2,6],[1,3,5],[2,3,4]]


def test3():
    print(Solution().combinationSum3(4, 1))  # []


test1()
test2()
test3()
