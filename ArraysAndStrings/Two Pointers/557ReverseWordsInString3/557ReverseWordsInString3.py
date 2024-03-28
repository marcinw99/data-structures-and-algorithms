class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        result = []
        left = 0
        right = 0

        while left <= n:
            while right < n - 1 and not s[right + 1].isspace():
                right += 1
            new_word = []
            for i in range(right, left-1, -1):
                new_word.append(s[i])
            result.append("".join(new_word))
            right += 2
            left = right

        return " ".join(result)


def test1():
    print(Solution().reverseWords("Let's take LeetCode contest"))  # "s'teL ekat edoCteeL tsetnoc"


def test2():
    print(Solution().reverseWords("Mr Ding"))  # "rM gniD"


test1()
test2()
