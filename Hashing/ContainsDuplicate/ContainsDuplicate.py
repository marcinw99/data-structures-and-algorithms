from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False

    def containsDuplicateSet(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


def test1():
    print(Solution().containsDuplicate([1, 2, 3, 1]))  # True


test1()
