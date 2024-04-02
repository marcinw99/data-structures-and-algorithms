from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] + nums[i])
        self.prefix = prefix

    def sumRange(self, left: int, right: int) -> int:
        sum_up_to_right = self.prefix[right]
        left_outside = self.prefix[left - 1] if left > 0 else 0
        return sum_up_to_right - left_outside


def test1():
    arr = NumArray([-2, 0, 3, -5, 2, -1])
    print(arr.sumRange(0, 2))  # 1
    print(arr.sumRange(2, 5))  # -1
    print(arr.sumRange(0, 5))  # -3


test1()
