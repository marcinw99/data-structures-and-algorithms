from typing import List


def findMaxLength(nums: List[int]) -> int:
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i - 1])

    answer = 0

    for i in range(len(prefix) - 1, -1, -1):
        furthestIndex = (prefix[i] * 2) - i - 1

        j = furthestIndex
        while j < i and i - j + 1 > answer:
            currentSum = prefix[i]
            if j > 0:
                currentSum -= prefix[j - 1]

            length = i - j + 1

            if currentSum * 2 == length:
                answer = max(answer, length)

            j += 1

    return answer


print(findMaxLength([0, 1]))  # 2
print(findMaxLength([0, 1, 0]))  # 2
print(findMaxLength([0, 1, 0, 1]))  # 4
print(findMaxLength([0, 0, 1, 0]))  # 2
print(findMaxLength([0, 0, 0, 1, 1, 1]))  # 6
print(findMaxLength([1, 1, 1, 0, 0, 0]))  # 6
print(findMaxLength([0, 0, 0, 0]))  # 0
print(findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))  # 6
print(findMaxLength(
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
     1,
     0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0,
     1,
     0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1]))
