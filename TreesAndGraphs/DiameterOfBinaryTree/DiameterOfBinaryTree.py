class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: TreeNode) -> int:
    def dfs(node: TreeNode, max_diameter: int) -> (int, int):
        if node is None:
            return -1, max_diameter

        left, left_max_diameter = dfs(node.left, max_diameter)
        right, right_max_diameter = dfs(node.right, max_diameter)

        left_length = left + 1
        right_length = right + 1

        return max(left_length, right_length), max(left_length + right_length, left_max_diameter, right_max_diameter)

    result, max_diam = dfs(root, 0)

    return max_diam


def diameterOfBinaryTreeWhenImNotStupid(root: TreeNode) -> int:
    diameter = 0

    def dfs(node: TreeNode) -> int:
        if node is None:
            return 0

        left_length = dfs(node.left)
        right_length = dfs(node.right)

        nonlocal diameter
        diameter = max(left_length + right_length, diameter)

        return max(left_length, right_length) + 1

    dfs(root)

    return diameter


def test1():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    print(diameterOfBinaryTree(node1))


def test2():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node1.left = node2

    print(diameterOfBinaryTree(node1))


def test3():
    node1 = TreeNode(1)
    print(diameterOfBinaryTree(node1))


test1()  # 3
test2()  # 1
test3()  # 0
