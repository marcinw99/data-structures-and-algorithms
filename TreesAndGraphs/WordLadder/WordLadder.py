from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        visited = {beginWord}

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    potential_word = word[:i] + char + word[i + 1:]
                    if potential_word not in visited and potential_word in words:
                        visited.add(potential_word)
                        queue.append((potential_word, length + 1))
        return 0


def test1():
    print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5


def test2():
    print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0


def test3():
    print(Solution().ladderLength("hot", "dog", ["hot", "dog"]))  # 0


test1()
test2()
test3()
