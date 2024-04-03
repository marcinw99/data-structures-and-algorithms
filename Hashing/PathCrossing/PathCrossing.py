class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current_location = (0, 0)
        visited = {(0, 0)}

        direction_deltas = {
            "N": (0, -1),
            "S": (0, 1),
            "W": (-1, 0),
            "E": (1, 0),
        }

        for direction in path:
            dx, dy = direction_deltas[direction]
            next_location = (current_location[0] + dx, current_location[1] + dy)
            if next_location in visited:
                return True
            visited.add(next_location)
            current_location = next_location

        return False


def test1():
    print(Solution().isPathCrossing("NES"))  # False


def test2():
    print(Solution().isPathCrossing("NESWW"))  # True


test1()
test2()
