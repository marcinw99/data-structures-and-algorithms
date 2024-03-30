from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        pointer1 = 0
        pointer2 = 0

        while pointer1 < n and pointer2 < m:
            num1 = nums1[pointer1]
            num2 = nums2[pointer2]

            if num1 == num2:
                return num1

            if num1 < num2:
                pointer1 += 1
            else:
                pointer2 += 1

        return -1


def test1():
    print(Solution().getCommon([1, 2, 3], [2, 4]))  # 2


def test2():
    print(Solution().getCommon([1, 2, 3, 6], [2, 3, 4, 5]))  # 2


test1()
test2()
