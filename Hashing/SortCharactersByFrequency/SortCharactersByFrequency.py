from collections import deque


class Solution:
    def frequencySortFirst(self, s: str) -> str:
        frequencies = {}

        for char in s:
            frequency = frequencies.get(char, 0) + 1
            frequencies[char] = frequency

        queue = []
        i = 0
        for char, frequency in frequencies.items():
            if not queue:
                queue.append((char, frequency))
            else:
                while i < len(queue) and queue[i][1] < frequency:
                    i += 1
                queue.insert(i, (char, frequency))
                i = 0

        # potentially built-in sort function using frequency

        result = []

        while queue:
            char, frequency = queue.pop()
            for i in range(frequency):
                result.append(char)

        return "".join(result)

    def frequencySort(self, s: str) -> str:
        frequencies = {}

        for char in s:
            frequency = frequencies.get(char, 0) + 1
            frequencies[char] = frequency

        queue = [[char, frequency] for char, frequency in frequencies.items()]
        queue = sorted(queue, key=lambda item: item[1])

        result = []

        while queue:
            char, frequency = queue.pop()
            for i in range(frequency):
                result.append(char)

        return "".join(result)


def test1():
    print(Solution().frequencySort("tree"))  # "eert"


def test2():
    print(Solution().frequencySort("cccaaa"))  # "aaaccc"


def test3():
    print(Solution().frequencySort("Aabb"))  # "bbAa"


def test4():
    print(Solution().frequencySort("raaeaedere"))  # "eeeeaaarrd"


test1()
test2()
test3()
test4()
