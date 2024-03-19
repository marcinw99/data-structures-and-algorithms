from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(max_sum):
            current = 0
            splits_count = 0

            for num in nums:
                if current + num <= max_sum:
                    current += num
                else:
                    current = num
                    splits_count += 1

            return splits_count + 1

        left = max(nums)
        right = sum(nums)
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            if check(mid) <= k:
                right = mid - 1
                answer = mid
            else:
                left = mid + 1

        return answer


def test1():
    print(Solution().splitArray([7, 2, 5, 10, 8], 2))  # 18


def test2():
    print(Solution().splitArray([1, 2, 3, 4, 5], 2))  # 9


test1()
test2()
