class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        n = len(s)
        right = 0
        current = 1 if s[0] in vowels else 0

        while right < k - 1:
            right += 1
            if s[right] in vowels:
                current += 1
        answer = current

        while right < n - 1:
            right += 1
            if s[right - k] in vowels:
                current -= 1
            if s[right] in vowels:
                current += 1
            answer = max(answer, current)

        return answer

    def maxVowelsCleaner(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        n = len(s)
        current = 0

        for i in range(k):
            if s[i] in vowels:
                current += 1
        answer = current

        for right in range(k, n):
            if s[right - k] in vowels:
                current -= 1
            if s[right] in vowels:
                current += 1
            answer = max(answer, current)

        return answer


def test1():
    print(Solution().maxVowelsCleaner("abciiidef", 3))  # 3


def test2():
    print(Solution().maxVowelsCleaner("aeiou", 2))  # 2


def test3():
    print(Solution().maxVowelsCleaner("leetcode", 3))  # 2
    print(Solution().maxVowelsCleaner("weallloveyou", 7))  # 4


test1()
test2()
test3()
