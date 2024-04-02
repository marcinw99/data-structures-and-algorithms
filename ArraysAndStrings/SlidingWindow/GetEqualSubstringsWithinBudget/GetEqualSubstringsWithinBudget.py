class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        left = 0
        answer = current_cost = 0

        for right in range(n):
            current_cost += abs(ord(s[right]) - ord(t[right]))

            while current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            answer = max(answer, right - left + 1)

        return answer


def test1():
    print(Solution().equalSubstring("abcd", "bcdf", 3))  # 3


def test2():
    print(Solution().equalSubstring("abcd", "cdef", 3))  # 1


def test3():
    print(Solution().equalSubstring("abcd", "acde", 0))  # 1


test1()
test2()
test3()
