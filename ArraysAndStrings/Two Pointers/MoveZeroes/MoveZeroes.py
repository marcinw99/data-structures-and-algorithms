from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        nearest_zero = -1
        nearest_num = -1

        for i in range(n):
            if nums[i] == 0:
                nearest_zero = i
                break

        for i in range(nearest_zero, n):
            if nums[i] != 0:
                nearest_num = i
                break

        if -1 in [nearest_zero, nearest_num]:
            return

        while nearest_num < n:
            nums[nearest_zero] = nums[nearest_num]
            nums[nearest_num] = 0
            nearest_zero += 1
            while nearest_num < n and nums[nearest_num] == 0:
                nearest_num += 1

    def moveZeroesBetter(self, nums: List[int]) -> None:
        n = len(nums)
        left = 0

        for right in range(n):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1


def test1():
    value = [0, 1, 0, 3, 12]
    Solution().moveZeroesBetter(value)
    print(value)  # [1,3,12,0,0]


def test2():
    value = [0]
    Solution().moveZeroesBetter(value)
    print(value)  # [0]


def test3():
    value = [2, 1]
    Solution().moveZeroesBetter(value)
    print(value)  # [2,1]


def test4():
    value = [0, 1, 1, 0]
    Solution().moveZeroesBetter(value)
    print(value)  # [1,1,0,0]


def test5():
    value = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    Solution().moveZeroesBetter(value)
    print(value)  # [4,2,4,3,5,1,0,0,0,0]


test1()
test2()
# test3()
# test4()
# test5()
