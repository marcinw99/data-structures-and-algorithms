from queue import Queue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: TreeNode) -> int:
    def findMinDepth(node: TreeNode, depth_so_far: int) -> Optional[int]:
        if not node:
            return None

        if not node.left and not node.right:
            return depth_so_far

        next_depth = depth_so_far + 1
        left = findMinDepth(node.left, next_depth)
        right = findMinDepth(node.right, next_depth)

        if left and right:
            return min(left, right)

        if left:
            return left

        return right

    return findMinDepth(root, 1) or 0


def minDepthFromLC(root: TreeNode) -> int:
    def dfs(node: TreeNode) -> int:
        if not node:
            return 0

        if not node.left:
            return 1 + dfs(node.right)
        elif not node.right:
            return 1 + dfs(node.left)

        return 1 + min(dfs(node.left), dfs(node.right))

    return dfs(root)


# does not work
def minDepthBFS(root: TreeNode) -> int:
    if not root:
        return 0

    q = Queue()
    q.put(root)
    depth = 1

    while not q.empty():
        level_size = q.qsize()

        for _ in range(level_size):
            node = q.get()

            if not node:
                continue

            if not node.left and not node.right:
                return depth

            q.put(node.left)
            q.put(node.right)
        depth += 1

    return -1


node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node1.left = node2
node1.right = node3
node4 = TreeNode(15)
node5 = TreeNode(7)
node3.left = node4
node3.right = node5

print(minDepth(node1))
