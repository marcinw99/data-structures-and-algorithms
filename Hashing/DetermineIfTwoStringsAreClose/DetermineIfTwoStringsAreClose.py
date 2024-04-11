class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1map = {}
        word2map = {}
        word2_frequencies = []

        for char in word1:
            word1map[char] = word1map.get(char, 0) + 1

        for char in word2:
            word2map[char] = word2map.get(char, 0) + 1

        for char in word2map:
            word2_frequencies.append(word2map[char])

        for char in word1map:
            frequency = word1map[char]

            if frequency not in word2_frequencies:
                return False
            else:
                word2_frequencies.remove(frequency)

            if char not in word2map:
                return False

        return True


def test1():
    print(Solution().closeStrings("abc", "bca"))  # True


def test2():
    print(Solution().closeStrings("a", "aa"))  # False


def test3():
    print(Solution().closeStrings("cabbba", "abbccc"))  # True


test1()
test2()
test3()
