from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        answer = []

        def backtrack(current, i):
            if i == len(digits):
                answer.append("".join(current[:]))
                return

            for character in letters[digits[i]]:
                current.append(character)
                backtrack(current, i + 1)
                current.pop()

        backtrack([], 0)

        return answer


def test1():
    print(Solution().letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]


def test2():
    print(Solution().letterCombinations(""))  # []


def test3():
    print(Solution().letterCombinations("2"))  # ["a","b","c"]


test1()
test2()
test3()
