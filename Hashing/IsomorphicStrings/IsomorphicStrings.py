class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sources_map = {}
        targets_map = {}

        for i in range(len(s)):
            if s[i] in sources_map and sources_map[s[i]] != t[i]:
                return False
            if t[i] in targets_map and targets_map[t[i]] != s[i]:
                return False
            sources_map[s[i]] = t[i]
            targets_map[t[i]] = s[i]

        return True

    # from LC
    def transformString(self, s: str) -> str:
        index_mapping = {}
        new_str = []

        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))

        return " ".join(new_str)

    def isIsomorphicFromLC(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)


def test1():
    print(Solution().isIsomorphic("egg", "add"))  # True


def test2():
    print(Solution().isIsomorphic("foo", "bar"))  # False


def test3():
    print(Solution().isIsomorphic("paper", "title"))  # True


def test4():
    print(Solution().isIsomorphic("badc", "baba"))  # False


def test5():
    print(Solution().isIsomorphic("egcd", "adfd"))  # False


test1()
test2()
test3()
test4()
test5()
