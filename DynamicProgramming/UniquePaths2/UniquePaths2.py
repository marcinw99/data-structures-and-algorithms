from functools import cache
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def dp(row, col):
            if obstacleGrid[row][col] == 1:
                return 0

            if row + col == 0:
                return 1

            answer = 0

            if row > 0 and obstacleGrid[row - 1][col] != 1:
                answer += dp(row - 1, col)
            if col > 0 and obstacleGrid[row][col - 1] != 1:
                answer += dp(row, col - 1)

            return answer

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        return dp(n - 1, m - 1)

    def uniquePathsWithObstaclesBottomUp(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        if obstacleGrid[n - 1][m - 1] == 1:
            return 0

        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1

        for row in range(n):
            for col in range(m):
                answer = 0
                if row > 0 and obstacleGrid[row - 1][col] != 1:
                    answer += dp[row - 1][col]
                if col > 0 and obstacleGrid[row][col - 1] != 1:
                    answer += dp[row][col - 1]
                dp[row][col] += answer

        return dp[n - 1][m - 1]

    def uniquePathsWithObstaclesBottomUpBetterSpace(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        if obstacleGrid[n - 1][m - 1] == 1:
            return 0

        dp = [0] * m
        dp[0] = 1

        for row in range(n):
            next_row = [0] * m
            for col in range(m):
                if row > 0 and obstacleGrid[row - 1][col] != 1:
                    next_row[col] += dp[col]
                if col > 0 and obstacleGrid[row][col - 1] != 1:
                    next_row[col] += next_row[col - 1]
            dp = next_row

        return dp[m - 1]

    def uniquePathsWithObstaclesBottomUpBetterSpace2(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [0] * m
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0

        for row in range(n):
            for col in range(m):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                else:
                    if col > 0:
                        dp[col] += dp[col - 1]

        return dp[m - 1]


def test1():
    print(Solution().uniquePathsWithObstaclesBottomUpBetterSpace2([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2


def test2():
    print(Solution().uniquePathsWithObstaclesBottomUpBetterSpace2([[0, 1], [0, 0]]))  # 1


def test3():
    print(Solution().uniquePathsWithObstaclesBottomUpBetterSpace2([[0, 0], [0, 1]]))  # 0
    print(Solution().uniquePathsWithObstaclesBottomUpBetterSpace2([[1]]))  # 0


test1()
# test2()
# test3()
