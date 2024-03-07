import math
from collections import deque
from typing import List


class Solution:
    def snakesAndLaddersFirst(self, board: List[List[int]]) -> int:
        size = len(board)

        def get_number_from_coords(row: int, col: int) -> int:
            row_multiplier = size - 1 - row
            col_addition = col + 1 if row_multiplier % 2 == 0 else size - col
            return row_multiplier * size + col_addition

        def get_coords_from_number(number: int) -> (int, int):
            row = size - 1 - math.floor((number - 1) / size)
            units = number % size or size
            col = units - 1 if row % 2 != 0 else size - units

            return row, col

        queue = deque([(size - 1, 0, 0)])
        visited = {(size - 1, 0)}

        while queue:
            row, col, moves = queue.popleft()

            if row == col == 0:
                return moves

            current_number = get_number_from_coords(row, col)
            for next_number in range(current_number + 1, min(current_number + 6, size * size)):

                next_row, next_col = get_coords_from_number(next_number)

                if (next_row, next_col) in visited:
                    continue

                visited.add((next_row, next_col))

                if board[next_row][next_col] != -1:
                    next_row_switched, next_col_switched = get_coords_from_number(board[next_row][next_col])
                    queue.append((next_row_switched, next_col_switched, moves + 1))
                else:
                    queue.append((next_row, next_col, moves + 1))

        return -1

    def snakesAndLaddersBetter(self, board: List[List[int]]) -> int:
        size = len(board)
        target = size * size
        coords_per_number = {}
        for i in range(size):
            for j in range(size):
                row = size - 1 - i
                col = j if i % 2 == 0 else size - 1 - j
                coords_per_number[i * size + j + 1] = (row, col)

        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            current_number, moves = queue.popleft()
            for next_number in range(current_number + 1, min(current_number + 7, target + 1)):
                if next_number == target:
                    return moves + 1
                next_row, next_col = coords_per_number[next_number]

                if board[next_row][next_col] != -1:
                    next_number_switched = board[next_row][next_col]
                    if next_number_switched == target:
                        return moves + 1
                    if next_number_switched not in visited:
                        visited.add(next_number_switched)
                        queue.append((next_number_switched, moves + 1))
                elif next_number not in visited:
                    visited.add(next_number)
                    queue.append((next_number, moves + 1))
        return -1


def test1():
    print(Solution().snakesAndLaddersBetter(
        [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]
    ))  # 4


def test2():
    print(Solution().snakesAndLaddersBetter([[-1, -1], [-1, 3]]
                                            ))  # 1


def test3():
    print(Solution().snakesAndLaddersBetter([[-1, 4, -1], [6, 2, 6], [-1, 3, -1]]
                                            ))  # 2


def test4():
    print(Solution().snakesAndLaddersBetter([[1, 1, -1], [1, 1, 1], [-1, 1, 1]]
                                            ))  # -1


test1()
test2()
test3()
test4()
