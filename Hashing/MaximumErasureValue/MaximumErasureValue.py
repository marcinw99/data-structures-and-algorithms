from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = current = answer = 0
        frequencies = {}

        for right in range(n):
            num = nums[right]
            current += num
            frequency = frequencies.get(num, 0) + 1
            frequencies[num] = frequency

            while frequencies[num] > 1:
                current -= nums[left]
                frequencies[nums[left]] -= 1
                left += 1

            answer = max(answer, current)

        return answer


def test1():
    print(Solution().maximumUniqueSubarray([4, 2, 4, 5, 6]))  # 17


def test2():
    print(Solution().maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))  # 8


test1()
test2()
