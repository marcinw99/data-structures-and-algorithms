class Solution:
    # two pointers
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        s_list = list(s)
        left = 0
        right = n - 1

        while left < right:
            while not s[left].isalpha() and left < n - 1:
                left += 1
            while not s[right].isalpha() and right > 0:
                right -= 1

            if not s[left].isalpha() or not s[right].isalpha():
                continue

            s_list[left] = s[right]
            s_list[right] = s[left]
            left += 1
            right -= 1

        return "".join(s_list)

    # stack
    def reverseOnlyLettersStack(self, s: str) -> str:
        allowed_characters = [c for c in s if c.isalpha()]
        result = []

        for c in s:
            if c.isalpha():
                result.append(allowed_characters.pop())
            else:
                result.append(c)

        return "".join(result)

    def reverseOnlyLettersSinglePointer(self, s: str) -> str:
        n = len(s)
        right = n - 1
        result = list(s)

        for i in range(n):
            if i > right:
                continue

            while not s[right].isalpha() and right > 0:
                right -= 1

            if s[i].isalpha():
                result[i] = s[right]
                result[right] = s[i]
                right -= 1

        return "".join(result)


def test1():
    print(Solution().reverseOnlyLettersSinglePointer("ab-cd"))  # dc-ba


def test2():
    print(Solution().reverseOnlyLettersSinglePointer("a-bC-dEf-ghIj"))  # j-Ih-gfE-dCba


def test3():
    print(Solution().reverseOnlyLettersSinglePointer("Test1ng-Leet=code-Q!"))  # Qedo1ct-eeLg=ntse-T!


def test4():
    print(Solution().reverseOnlyLettersSinglePointer("7_28]"))  # 7_28]


# test1()
test2()
# test3()
# test4()
