from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing_cities = set()
        destination_cities = set()

        for a, b in paths:
            outgoing_cities.add(a)
            if b not in outgoing_cities:
                destination_cities.add(b)

        for destination_city in destination_cities:
            if destination_city not in outgoing_cities:
                return destination_city

        return ""


def test1():
    print(Solution().destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))  # Sao Paulo


def test2():
    print(Solution().destCity([["B", "C"], ["D", "B"], ["C", "A"]]))  # A


def test3():
    print(Solution().destCity([["A", "Z"]]))  # Z


test1()
test2()
test3()
