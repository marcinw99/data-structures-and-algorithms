from functools import cache
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        @cache
        def dp(row, col):
            if row == 0:
                return matrix[row][col]

            answer = dp(row - 1, col)
            if col > 0:
                answer = min(answer, dp(row - 1, col - 1))
            if col < m - 1:
                answer = min(answer, dp(row - 1, col + 1))
            return answer + matrix[row][col]

        return min([dp(n - 1, i) for i in range(m)])

    def minFallingPathSumBottomUp(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * m for _ in range(n)]
        for i in range(m):
            dp[0][i] = matrix[0][i]

        for row in range(1, n):
            for col in range(m):
                dp[row][col] = dp[row - 1][col]
                if col > 0:
                    dp[row][col] = min(dp[row][col], dp[row - 1][col - 1])
                if col < m - 1:
                    dp[row][col] = min(dp[row][col], dp[row - 1][col + 1])
                dp[row][col] += matrix[row][col]

        return min(dp[n - 1])


def test1():
    print(Solution().minFallingPathSumBottomUp([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))  # 13


def test2():
    print(Solution().minFallingPathSumBottomUp([[-19, 57], [-40, -5]]))  # -59


test1()
test2()
