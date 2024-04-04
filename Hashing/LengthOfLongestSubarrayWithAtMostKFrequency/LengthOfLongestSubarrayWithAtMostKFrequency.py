from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        frequencies = {}
        answer = 0
        for right in range(n):
            new_num = nums[right]
            frequency = frequencies.get(new_num, 0) + 1
            frequencies[new_num] = frequency

            while frequencies[new_num] > k:
                removed_num = nums[left]
                removed_num_frequency = frequencies.get(removed_num) - 1
                frequencies[removed_num] = removed_num_frequency
                left += 1
            answer = max(answer, right - left + 1)

        return answer


def test1():
    print(Solution().maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2))  # 6


def test2():
    print(Solution().maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1))  # 2


def test3():
    print(Solution().maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4))  # 4


test1()
test2()
test3()
