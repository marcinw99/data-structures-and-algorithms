def simplifyPath(path: str) -> str:
    canonicalPathStack = ['/']

    for char in path + '/':
        if char == '/':
            if canonicalPathStack[-1] == '.' and canonicalPathStack[-2] == '.' and canonicalPathStack[-3] == '/':
                canonicalPathStack.pop()
                canonicalPathStack.pop()
                if len(canonicalPathStack) > 1:
                    canonicalPathStack.pop()
                    while canonicalPathStack[-1] != '/':
                        canonicalPathStack.pop()
            elif canonicalPathStack[-1] == '.' and canonicalPathStack[-2] == '/':
                canonicalPathStack.pop()
            elif canonicalPathStack[-1] != '/':
                canonicalPathStack.append(char)
        else:
            canonicalPathStack.append(char)

    if canonicalPathStack[-1] == '/' and len(canonicalPathStack) > 1:
        canonicalPathStack.pop()

    return ''.join(canonicalPathStack)


# print(simplifyPath('/home/'))  # /home
# print(simplifyPath('/../'))  # /
# print(simplifyPath('/home//foo'))  # /home/foo
# print(simplifyPath("/a/./b/../../c/"))  # /c
# print(simplifyPath("/a/../../b/../c//.//"))  # /c
print(simplifyPath("/a//b////c/d//././/.."))  # /a/b/c


def simplifyPathFromLC(path: str) -> str:
    # Initialize a stack
    stack = []

    # Split the input string on "/" as the delimiter
    # and process each portion one by one
    for portion in path.split("/"):

        # If the current component is a "..", then
        # we pop an entry from the stack if it's non-empty
        if portion == "..":
            if stack:
                stack.pop()
        elif portion == "." or not portion:
            # A no-op for a "." or an empty string
            continue
        else:
            # Finally, a legitimate directory name, so we add it
            # to our stack
            stack.append(portion)

    # Stich together all the directory names together
    final_str = "/" + "/".join(stack)
    return final_str
