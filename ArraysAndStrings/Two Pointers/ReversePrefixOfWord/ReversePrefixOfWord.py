class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)
        reversed_end = 0

        while word[reversed_end] != ch and reversed_end < n - 1:
            reversed_end += 1

        if word[reversed_end] != ch:
            return word

        natural_order_start = reversed_end + 1
        result = []

        while reversed_end >= 0:
            result.append(word[reversed_end])
            reversed_end -= 1

        while natural_order_start <= n - 1:
            result.append(word[natural_order_start])
            natural_order_start += 1

        return "".join(result)


def test1():
    print(Solution().reversePrefix("abcdefd", "d"))  # "dcbaefd"


def test2():
    print(Solution().reversePrefix("xyxzxe", "z"))  # "zxyxxe"


def test3():
    print(Solution().reversePrefix("abcd", "z"))  # "abcd"


test1()
test2()
test3()
