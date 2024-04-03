from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        visited_count = {}
        current = 0

        for num in nums:
            if num not in visited_count:
                current += num
                visited_count[num] = 1
            elif visited_count[num] == 1:
                current -= num
                visited_count[num] = 2

        return current


def test1():
    print(Solution().sumOfUnique([1, 2, 3, 2]))  # 4


def test2():
    print(Solution().sumOfUnique([1, 1, 1, 1, 1]))  # 0


def test3():
    print(Solution().sumOfUnique([1, 2, 3, 4, 5]))  # 15


test1()
test2()
test3()
