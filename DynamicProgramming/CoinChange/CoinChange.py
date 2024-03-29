from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        sorted_coins = sorted(coins, reverse=True)

        def dp(remaining_amount):
            if remaining_amount in cache:
                return cache[remaining_amount]

            if remaining_amount == 0:
                return 0

            fewest = float("+inf")
            for coin in sorted_coins:
                diff = remaining_amount - coin
                if diff >= 0:
                    count = dp(diff) + 1
                    fewest = min(count, fewest)

            cache[remaining_amount] = fewest
            return cache[remaining_amount]

        cache = {}
        result = dp(amount)
        return result if result != float("+inf") else -1


def test1():
    print(Solution().coinChange([1, 2, 5], 11))  # 3
    print(Solution().coinChange([3, 5], 11))  # 3


def test2():
    print(Solution().coinChange([2], 3))  # -1


def test3():
    print(Solution().coinChange([1], 0))  # 0


test1()
test2()
test3()
