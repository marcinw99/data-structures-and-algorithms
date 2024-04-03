from collections import defaultdict
from typing import List


class Solution:
    def maxFrequencyElementsWeird(self, nums: List[int]) -> int:
        frequencies = {}
        frequencies_numbers = defaultdict(list)
        highest_frequency = 0

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 1
                frequencies_numbers[1].append(num)
            else:
                frequencies_numbers[frequencies[num]].remove(num)
                frequencies[num] += 1
                frequencies_numbers[frequencies[num]].append(num)
            highest_frequency = max(highest_frequency, frequencies[num])

        return highest_frequency * len(frequencies_numbers[highest_frequency])

    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = {}
        highest_frequency = 0
        total_frequency = 0

        for num in nums:
            current_num_frequency = frequencies.get(num, 0) + 1
            frequencies[num] = current_num_frequency

            if current_num_frequency > highest_frequency:
                highest_frequency = current_num_frequency
                total_frequency = current_num_frequency
            elif current_num_frequency == highest_frequency:
                total_frequency += current_num_frequency

        return total_frequency


def test1():
    print(Solution().maxFrequencyElements([1, 2, 2, 3, 1, 4]))  # 4


def test2():
    print(Solution().maxFrequencyElements([1, 2, 3, 4, 5]))  # 5


test1()
test2()
