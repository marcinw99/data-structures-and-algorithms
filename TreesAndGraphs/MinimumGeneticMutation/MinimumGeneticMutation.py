from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene, 0)])
        visited = {startGene}
        bank_set = set(bank)

        def get_neighbours(initial_gene: str) -> List[str]:
            result = []

            for i in range(8):
                for fragment in ['A', 'C', 'G', 'T']:
                    potential_gene = initial_gene[:i] + fragment + initial_gene[i + 1:]
                    if potential_gene not in visited and potential_gene in bank_set:
                        result.append(potential_gene)

            return result

        while queue:
            gene, count = queue.popleft()

            if gene == endGene:
                return count

            for neighbour in get_neighbours(gene):
                visited.add(neighbour)
                queue.append((neighbour, count + 1))

        return -1


def test1():
    print(Solution().minMutation('AACCGGTT', 'AACCGGTA', ["AACCGGTA"]))  # 1


def test2():
    print(Solution().minMutation('AACCGGTT', 'AAACGGTA', ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))  # 2


def test3():
    print(Solution().minMutation("AACCGGTT",
                                 "AAACGGTA",
                                 ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]))  # 4


test1()
test2()
test3()
