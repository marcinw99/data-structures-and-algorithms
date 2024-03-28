from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 1:
                return 1
            if i == 2:
                return 2

            return dp(i - 1) + dp(i - 2)

        return dp(n)

    def climbStairsIterative(self, n: int) -> int:
        dp = [0] * (n + 2)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


def test1():
    print(Solution().climbStairsIterative(2))  # 2


def test2():
    print(Solution().climbStairsIterative(3))  # 3


test1()
test2()

# 1. takes i and returns ways count
# 2. count from prev one and one before prev one
# 3. 1 = 1

# 4
# 1 1 1 1
# 1 1 2
# 2 1 1
# 1 2 1
# 2 2
