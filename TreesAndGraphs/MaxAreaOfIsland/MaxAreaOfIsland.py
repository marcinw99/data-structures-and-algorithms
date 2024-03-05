from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        col_count = len(grid[0])

        answer = 0

        visited = set()

        directions_deltas = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def is_valid_neighbour(coords) -> bool:
            row, col = coords
            return 0 <= col < col_count and 0 <= row < row_count and grid[row][col] == 1

        def dfs(coords: (int, int)):
            nonlocal visited
            size = 1
            row, col = coords

            for neighbour_delta in directions_deltas:
                neighbour_coords = (row + neighbour_delta[0], col + neighbour_delta[1])
                if is_valid_neighbour(neighbour_coords) and neighbour_coords not in visited:
                    visited.add(neighbour_coords)
                    size += dfs(neighbour_coords)

            return size

        for row in range(row_count):
            for col in range(col_count):
                current_coords = (row, col)
                if grid[row][col] == 1 and current_coords not in visited:
                    visited.add(current_coords)
                    island_size = dfs(current_coords)
                    answer = max(answer, island_size)

        return answer

    def maxAreaOfIslandIterative(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        col_count = len(grid[0])

        answer = 0

        visited = set()

        directions_deltas = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def is_valid_neighbour(coords) -> bool:
            row, col = coords
            return 0 <= col < col_count and 0 <= row < row_count and grid[row][col] == 1

        def dfs(coords: (int, int)):
            nonlocal visited
            size = 1
            stack = [coords]

            while len(stack) > 0:
                current_coords = stack.pop()
                row, col = current_coords
                for neighbour_delta in directions_deltas:
                    neighbour_coords = (row + neighbour_delta[0], col + neighbour_delta[1])
                    if is_valid_neighbour(neighbour_coords) and neighbour_coords not in visited:
                        visited.add(neighbour_coords)
                        size += 1
                        stack.append(neighbour_coords)

            return size

        for row in range(row_count):
            for col in range(col_count):
                current_coords = (row, col)
                if grid[row][col] == 1 and current_coords not in visited:
                    visited.add(current_coords)
                    island_size = dfs(current_coords)
                    answer = max(answer, island_size)

        return answer


def test1():
    print(Solution().maxAreaOfIslandIterative(
        [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))  # 6


def test2():
    print(Solution().maxAreaOfIslandIterative([[0, 0, 0, 0, 0, 0, 0, 0]]))  # 0


test1()
test2()
