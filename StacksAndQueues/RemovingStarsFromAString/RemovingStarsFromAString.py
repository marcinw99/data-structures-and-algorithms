from collections import deque


class Solution:
    def removeStars(self, s: str) -> str:
        deq = deque()

        for character in s:
            if character != "*":
                deq.append(character)
            else:
                deq.pop()

        result = list(deq)

        return "".join(result)


def test1():
    print(Solution().removeStars("leet**cod*e"))  # lecoe


def test2():
    print(Solution().removeStars("erase*****"))  #


test1()
test2()
