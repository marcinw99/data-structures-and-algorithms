import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(x):
            nums_sum = 0
            for num in nums:
                nums_sum += math.ceil(num / x)
            return nums_sum <= threshold

        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


# O(n * log m)
# n - nums.length, m - max element of nums

def test1():
    print(Solution().smallestDivisor([1, 2, 5, 9], 6))  # 5


def test2():
    print(Solution().smallestDivisor([44, 22, 33, 11, 1], 5))  # 44


test1()
test2()
