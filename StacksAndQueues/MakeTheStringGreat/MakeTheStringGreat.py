def makeGood(s: str) -> str:
    stack = []

    for character in s:
        if not stack:
            stack.append(character)
        else:
            if character.isupper():
                if stack[-1].islower():
                    if character == stack[-1].upper():
                        stack.pop()
                        continue
            else:
                if stack[-1].isupper():
                    if character == stack[-1].lower():
                        stack.pop()
                        continue
            stack.append(character)

    return ''.join(stack)


def makeGoodBetter(s: str) -> str:
    stack = []

    for character in s:
        if stack and abs(ord(character) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(character)

    return ''.join(stack)


# print(makeGoodBetter('leEeetcode'))  # leetcode
# print(makeGoodBetter('abBAcC'))  #
# print(makeGoodBetter('s'))  # s


# from LC, without stack and O(n^2) but interesting
def makeGoodFromLCIteration(self, s: str) -> str:
    # if s has less than 2 characters, we just return itself.
    while len(s) > 1:
        # 'find' records if we find any pair to remove.
        find = False

        # Check every two adjacent characters, curr_char and next_char.
        for i in range(len(s) - 1):
            curr_char, next_char = s[i], s[i + 1]

            # If they make a pair, remove them from 's' and let 'find = True'.
            if abs(ord(curr_char) - ord(next_char)) == 32:
                s = s[:i] + s[i + 2:]
                find = True
                break

        # If we cannot find any pair to remove, break the loop.
        if not find:
            break
    return s


# jebana rekurencja
def makeGoodRecursion(self, s: str) -> str:
    # If we find a pair in 's', remove this pair from 's'
    # and solve the remaining string recursively.
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) == 32:
            return self.makeGood(s[:i] + s[i + 2:])

    # Base case, if we can't find a pair, just return 's'.
    return s


# mine solution if I knew that int difference between ascii chars and their uppercase counterparts is always 32
def makeGoodLCStack(self, s: str) -> str:
    # Use stack to store the visited characters.
    stack = []

    # Iterate over 's'.
    for curr_char in list(s):
        # If the current character make a pair with the last character in the stack,
        # remove both of them. Otherwise, we add the current character to stack.
        if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(curr_char)

    # Returns the string concatenated by all characters left in the stack.
    return "".join(stack)


# 2 pointers, in place modify

def makeGoodTwoPointers(s: str) -> str:
    dummy = list(s)

    end = 0
    for current in range(len(dummy)):
        if end > 0 and abs(ord(dummy[current]) - ord(dummy[end - 1])) == 32:
            end -= 1
        else:
            dummy[end] = dummy[current]
            end += 1

    return ''.join(dummy[0:end])


# print(makeGoodTwoPointers('leEtcode'))  # ltcode
# print(makeGoodTwoPointers('BbBbBb'))  #
# print(makeGoodTwoPointers('abBAcC'))  #
# print(makeGoodTwoPointers('s'))  # s

# T = O(n), S = O(1)