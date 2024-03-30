from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer = float("+inf")
        left = 0
        right = 0
        current = nums[0]
        n = len(nums)

        while right < n:
            while right < n - 1 and current < target:
                right += 1
                current += nums[right]

            while left < right and current - nums[left] >= target:
                current -= nums[left]
                left += 1

            if current >= target:
                answer = min(answer, right - left + 1)

            right += 1
            if right < n:
                current += nums[right]

        return answer if answer != float("+inf") else 0

    def minSubArrayLenBetter(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        answer = float("+inf")
        left = 0
        current = 0

        for right in range(n):
            current += nums[right]
            while current >= target:
                answer = min(answer, right - left + 1)
                current -= nums[left]
                left += 1

        return answer if answer != float("+inf") else 0


def test1():
    print(Solution().minSubArrayLenBetter(7, [2, 3, 1, 2, 4, 3]))  # 2


def test2():
    print(Solution().minSubArrayLenBetter(4, [1, 4, 4]))  # 1


def test3():
    print(Solution().minSubArrayLenBetter(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # 0


test1()
test2()
test3()
