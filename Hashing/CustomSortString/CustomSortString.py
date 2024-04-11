class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_ingredients = set(order)
        chars_frequency = {}
        unordered_chars = []

        for char in s:
            if char in order_ingredients:
                chars_frequency[char] = chars_frequency.get(char, 0) + 1
            else:
                unordered_chars.append(char)

        ordered_chars = []
        for char in order:
            if char in chars_frequency:
                frequency = chars_frequency[char]
                for _ in range(frequency):
                    ordered_chars.append(char)

        return "".join(ordered_chars + unordered_chars)


def test1():
    print(Solution().customSortString("cba", "abcd"))  # bcad


def test1():
    print(Solution().customSortString("bcafg", "abcd"))  # bcad


test1()
