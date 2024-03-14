from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        precompute = nums.copy()
        precompute.sort()
        for i in range(1, len(precompute)):
            precompute[i] += precompute[i - 1]

        def binary_search(input_arr: List[int], target: int) -> int:
            left, right = 0, len(input_arr)

            while left < right:
                mid = (left + right) // 2
                if input_arr[mid] > target:
                    right = mid
                else:
                    left = mid + 1

            return left

        answer = []
        for i, query in enumerate(queries):
            answer.append(binary_search(precompute, query))

        return answer


def test1():
    print(Solution().answerQueries([4, 5, 2, 1], [3, 10, 21]))  # 2,3,4


def test2():
    print(Solution().answerQueries([2, 3, 4, 5], [1]))  # 0


test1()
test2()
