from functools import cache
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        @cache
        def dp(i, holding):
            if i == n:
                return 0
            answer = dp(i + 1, holding)
            if holding:
                answer = max(answer, prices[i] - fee + dp(i + 1, False))
            else:
                answer = max(answer, -prices[i] + dp(i + 1, True))
            return answer

        return dp(0, False)

    def maxProfitBottomUp(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, 0] for __ in range(n + 1)]  # (holding / not holding) * n

        for i in range(n - 1, -1, -1):
            for j in [0, 1]:
                dp[i][j] = dp[i + 1][j]
                if j == 0:
                    # not holding -> buying
                    dp[i][j] = max(dp[i][j], -prices[i] + dp[i + 1][1])
                else:
                    # holding -> selling
                    dp[i][j] = max(dp[i][j], prices[i] - fee + dp[i + 1][0])

        return dp[0][0]

    def maxProfitBruhLCEditorial(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = -prices[0], 0

        for i in range(1, n):
            tmp = hold
            hold = max(hold, free - prices[i])
            free = max(free, tmp + prices[i] - fee)

        return free


def test1():
    print(Solution().maxProfitBottomUp([1, 3, 2, 8, 4, 9], 2))  # 8


def test2():
    print(Solution().maxProfitBottomUp([1, 3, 7, 5, 10, 3], 3))  # 6


test1()
test2()
