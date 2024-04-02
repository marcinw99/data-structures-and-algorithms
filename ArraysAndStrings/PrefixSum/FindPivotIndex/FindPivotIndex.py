from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(prefix[i - 1] + nums[i])

        for i in range(n):
            left = 0 if i == 0 else prefix[i - 1]
            right = prefix[n - 1] - prefix[i]
            if left == right:
                return i

        return -1


def test1():
    print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))  # 3


def test2():
    print(Solution().pivotIndex([1, 2, 3]))  # -1


def test3():
    print(Solution().pivotIndex([2, 1, -1]))  # 0


def test4():
    print(Solution().pivotIndex([-1, -1, -1, -1, -1, 0]))  # 2


test1()
test2()
test3()
test4()
