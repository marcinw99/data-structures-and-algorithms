class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        left = 0
        required_frequencies = {}
        current_frequencies = {}
        for char in s1:
            required_frequencies[char] = required_frequencies.get(char, 0) + 1

        for right in range(n):
            new_char = s2[right]
            current_frequencies[new_char] = current_frequencies.get(new_char, 0) + 1

            if new_char not in required_frequencies:
                while current_frequencies[new_char] > 0:
                    removed_char = s2[left]
                    current_frequencies[removed_char] = current_frequencies[removed_char] - 1
                    left += 1
            elif current_frequencies[new_char] > required_frequencies[new_char]:
                while current_frequencies[new_char] > required_frequencies[new_char]:
                    removed_char = s2[left]
                    current_frequencies[removed_char] = current_frequencies[removed_char] - 1
                    left += 1

            if right - left + 1 == len(s1):
                return True

        return False


def test1():
    print(Solution().checkInclusion("ab", "eidbaooo"))  # True


def test2():
    print(Solution().checkInclusion("ab", "eidboaoo"))  # False


test1()
test2()
