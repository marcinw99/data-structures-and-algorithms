from typing import List


class Solution:
    def numIdenticalPairsFirst(self, nums: List[int]) -> int:
        frequencies = {}
        for num in nums:
            frequency = frequencies.get(num, 0) + 1
            frequencies[num] = frequency

        answer = 0
        for _, count in frequencies.items():
            pairs_sum = count * (count - 1) // 2
            answer += pairs_sum

        return answer

    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequencies = {}
        answer = 0

        for num in nums:
            frequency = frequencies.get(num, 0) + 1
            frequencies[num] = frequency
            answer += frequency - 1

        return answer


def test1():
    print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # 4


def test2():
    print(Solution().numIdenticalPairs([1, 1, 1, 1]))  # 6


def test3():
    print(Solution().numIdenticalPairs([1, 2, 3]))  # 0


test1()
test2()
test3()
