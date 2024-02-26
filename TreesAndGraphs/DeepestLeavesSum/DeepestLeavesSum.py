from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deepest_leaves_sum(root: TreeNode) -> int:
    if not root:
        return 0

    queue = deque([root])
    last_sum = 0

    while len(queue):
        level_length = len(queue)
        current_level_sum = 0

        for _ in range(level_length):
            node = queue.popleft()
            current_level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        last_sum = current_level_sum

    return last_sum


def deepest_leaves_sum_dfs(root: TreeNode) -> int:
    max_depth = 0
    answer = 0

    def dfs(node: TreeNode, depth: int):
        nonlocal max_depth, answer
        if not node:
            return
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
        if max_depth < depth:
            max_depth = depth
        if depth == max_depth:
            answer += node.val

    dfs(root, 0)

    return answer


def test1():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    node4.left = node7
    node6.right = node8

    print(deepest_leaves_sum_dfs(node1))


test1()
