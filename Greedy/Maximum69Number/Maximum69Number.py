class Solution:
    def maximum69Number(self, num: int) -> int:
        number_as_string = str(num)

        for i in range(len(number_as_string)):
            if number_as_string[i] == '6':
                return int(number_as_string[:i] + "9" + number_as_string[i + 1:])

        return num


def test1():
    print(Solution().maximum69Number(9669))  # 9969


def test2():
    print(Solution().maximum69Number(9996))  # 9999


def test3():
    print(Solution().maximum69Number(9999))  # 9999


test1()
test2()
test3()
