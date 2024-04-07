from typing import List


class Solution:
    # time limit exceeded
    def numSubarraysWithSumTooLong(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        left = right = current = answer = 0

        while right < n:
            current += nums[right]
            right += 1
            if current < goal:
                continue

            while current > goal:
                removed_num = nums[left]
                current -= removed_num
                left += 1

            left_bound = left
            balance = 0
            while left_bound < right and balance == 0:
                answer += 1
                balance -= nums[left_bound]
                left_bound += 1

        return answer

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        prefix_with_frequencies = {0: 1}

        current = total_count = 0
        for i in range(n):
            current += nums[i]

            if current - goal in prefix_with_frequencies:
                left_bound_frequency = prefix_with_frequencies[current - goal]
                total_count += left_bound_frequency

            current_frequency = prefix_with_frequencies.get(current, 0) + 1
            prefix_with_frequencies[current] = current_frequency

        return total_count


def test1():
    print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2))  # 4


def test2():
    print(Solution().numSubarraysWithSum([0, 0, 0, 0, 0], 0))  # 15


def test3():
    print(Solution().numSubarraysWithSum([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 0))  # 27


test1()
test2()
test3()
