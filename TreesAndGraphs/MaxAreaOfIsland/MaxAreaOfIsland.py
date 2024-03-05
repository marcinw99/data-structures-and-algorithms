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

    def maxAreaOfIslandCleaner(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        column_count = len(grid[0])
        visited = set()

        def is_valid_island(row, column) -> bool:
            return 0 <= row < row_count and 0 <= column < column_count and (row, column) not in visited and grid[row][
                column] == 1

        def dfs(row, column):
            if is_valid_island(row, column):
                visited.add((row, column))
                return 1 + dfs(row + 1, column) + dfs(row - 1, column) + dfs(row, column - 1) + dfs(row, column + 1)
            else:
                return 0

        return max(dfs(row, column) for row in range(row_count) for column in range(column_count))

    def maxAreaOfIslandIterativeCleaner(self, grid):
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans


def test1():
    print(Solution().maxAreaOfIslandCleaner(
        [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))  # 6


def test2():
    print(Solution().maxAreaOfIslandCleaner([[0, 0, 0, 0, 0, 0, 0, 0]]))  # 0


test1()
test2()
