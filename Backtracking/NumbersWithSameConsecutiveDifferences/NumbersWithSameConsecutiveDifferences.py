from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        answer = []

        def backtrack(current):
            if len(current) == n:
                text = "".join(str(e) for e in current)
                num = int(text)
                if num not in answer:
                    answer.append(num)
                return

            last = current[-1]

            if last - k >= 0:
                current.append(last - k)
                backtrack(current)
                current.pop()

            if last + k < 10:
                current.append(last + k)
                backtrack(current)
                current.pop()

        for i in range(1, 10):
            backtrack([i])

        return answer

    def numsSameConsecDiffDFSFromLC(self, N: int, K: int) -> List[int]:

        if N == 1:
            return [i for i in range(10)]

        ans = []

        def DFS(N, num):
            # base case
            if N == 0:
                return ans.append(num)

            tail_digit = num % 10
            # using set() to avoid duplicates when K == 0
            next_digits = set([tail_digit + K, tail_digit - K])

            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    DFS(N - 1, new_num)

        for num in range(1, 10):
            DFS(N - 1, num)

        return list(ans)


def test1():
    print(Solution().numsSameConsecDiff(3, 7))  # [181,292,707,818,929]


def test2():
    print(Solution().numsSameConsecDiff(2, 1))  # [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


def test3():
    print(Solution().numsSameConsecDiff(2, 0))


test1()
test2()
test3()
