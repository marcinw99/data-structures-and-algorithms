from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque([(entrance[0], entrance[1], 0)])
        visited = {entrance[0], entrance[1]}

        def is_valid(row: int, col: int):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == "."

        def is_exit(next_row: int, next_col: int, current_row: int, current_col: int):
            if current_row == entrance[0] and current_col == entrance[1]:
                return False
            return not (0 <= next_row < m and 0 <= next_col < n)

        while queue:
            row, col, steps = queue.popleft()

            for dx, dy in directions:
                next_row, next_column = row + dx, col + dy
                if is_exit(next_row, next_column, row, col):
                    return steps
                elif is_valid(next_row, next_column) and (next_row, next_column) not in visited:
                    visited.add((next_row, next_column))
                    queue.append((next_row, next_column, steps + 1))

        return -1


def test1():
    print(Solution().nearestExit([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]))  # 1


def test2():
    print(Solution().nearestExit([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]))  # 2


def test3():
    print(Solution().nearestExit([[".", "+"]], [0, 0]))  # -1


def test4():
    print(Solution().nearestExit(
        [["+", ".", "+", "+", "+", "+", "+"], ["+", ".", "+", ".", ".", ".", "+"], ["+", ".", "+", ".", "+", ".", "+"],
         ["+", ".", ".", ".", "+", ".", "+"], ["+", "+", "+", "+", "+", "+", "."]], [0, 1]))  # ?


test1()
test2()
test3()
test4()

# ["+", ".", "+", "+", "+", "+", "+"]
# ["+", ".", "+", ".", ".", ".", "+"]
# ["+", ".", "+", ".", "+", ".", "+"]
# ["+", ".", ".", ".", "+", ".", "+"]
# ["+", "+", "+", "+", "+", "+", "."]
