from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for __ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            for j in [0, 1]:  # not holding, holding
                dp[i][j] = dp[i + 1][j]
                if j == 0:
                    # not holding -> buying
                    dp[i][j] = max(dp[i][j], -prices[i] + dp[i + 1][1])
                else:
                    # holding -> selling
                    dp[i][j] = max(dp[i][j], prices[i] + dp[i + 2][0])

        return dp[0][0]


def test1():
    print(Solution().maxProfit([1, 2, 3, 0, 2]))  # 3


def test2():
    print(Solution().maxProfit([1]))  # 0


test1()
test2()
