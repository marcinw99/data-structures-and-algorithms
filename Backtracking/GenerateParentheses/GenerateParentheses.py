from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(current):
            if len(current) == n * 2:
                answer.append(current)
                return

            openings = 0
            for char in current:
                if char == "(":
                    openings += 1

            if openings < n:
                backtrack(current + "(")
            if openings > len(current) / 2:
                backtrack(current + ")")

        answer = []

        backtrack("(")

        return answer

    def generateParenthesisBetter(self, n: int) -> List[str]:

        def backtrack(current, opening_count, closing_count):
            if len(current) == n * 2:
                answer.append("".join(current))
                return

            if opening_count < n:
                current.append("(")
                backtrack(current, opening_count + 1, closing_count)
                current.pop()
            if closing_count < opening_count:
                current.append(")")
                backtrack(current, opening_count, closing_count + 1)
                current.pop()

        answer = []

        backtrack([], 0, 0)

        return answer


def test1():
    print(Solution().generateParenthesisBetter(3))  # ["((()))","(()())","(())()","()(())","()()()"]


def test2():
    print(Solution().generateParenthesisBetter(1))  # ["()"]


test1()
test2()
