class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(s)
        current_word = []
        word_per_letter = {}
        assigned_words = set()
        position = 0
        for right in range(n):
            if position >= len(pattern):
                return False

            if s[right].isspace() or right == n - 1:
                if right == n - 1:
                    current_word.append(s[right])
                word = "".join(current_word)
                letter = pattern[position]
                if letter in word_per_letter and word != word_per_letter[letter]:
                    return False
                if letter not in word_per_letter:
                    if word in assigned_words:
                        return False
                    else:
                        word_per_letter[letter] = word
                        assigned_words.add(word)

                current_word = []
                position += 1
            else:
                current_word.append(s[right])

        return len(pattern) == position

    def wordPatternSplit(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        char_per_word = {}
        word_per_char = {}

        for i, char in enumerate(pattern):
            word = words[i]
            if word not in char_per_word and char not in word_per_char:
                word_per_char[char] = word
                char_per_word[word] = char
            if word in char_per_word and char in word_per_char and word_per_char[char] != word:
                return False
            if word not in char_per_word and char in word_per_char:
                return False
            if word in char_per_word and char not in word_per_char:
                return False

        return True


def test1():
    print(Solution().wordPatternSplit("abba", "dog cat cat dog"))  # True


def test2():
    print(Solution().wordPatternSplit("abba", "dog cat cat fish"))  # False


def test3():
    print(Solution().wordPatternSplit("aaaa", "dog cat cat dog"))  # False
    print(Solution().wordPatternSplit("aba", "dog cat cat"))  # False


def test4():
    print(Solution().wordPatternSplit("aaa", "aa aa aa aa"))  # False
    print(Solution().wordPatternSplit("jquery", "jquery"))  # False


test1()
test2()
test3()
test4()
