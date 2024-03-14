from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]

            if num == target:
                return mid

            if num > target:
                right = mid - 1

            if num < target:
                left = mid + 1

        return left


def test1():
    print(Solution().searchInsert([1, 3, 5, 6], 5))  # 2


def test2():
    print(Solution().searchInsert([1, 3, 5, 6], 2))  # 1


def test3():
    print(Solution().searchInsert([1, 3, 5, 6], 7))  # 4


test1()
test2()
test3()
