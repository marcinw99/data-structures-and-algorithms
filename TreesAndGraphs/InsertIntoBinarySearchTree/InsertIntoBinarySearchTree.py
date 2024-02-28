from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(val)

    def dfs(node: Optional[TreeNode]):
        nonlocal val

        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                dfs(node.left)
        else:
            if not node.right:
                node.right = TreeNode(val)
            else:
                dfs(node.right)
        return

    dfs(root)

    return root


def insertIntoBSTFromLC(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(val)

    if val > root.val:
        root.right = insertIntoBSTFromLC(root.right, val)
    else:
        root.left = insertIntoBSTFromLC(root.left, val)
    return root


def insertIntoBSTIterativeFromLC(root: TreeNode, val: int) -> TreeNode:
    node = root
    while node:
        # insert into the right subtree
        if val > node.val:
            # insert right now
            if not node.right:
                node.right = TreeNode(val)
                return root
            else:
                node = node.right
        # insert into the left subtree
        else:
            # insert right now
            if not node.left:
                node.left = TreeNode(val)
                return root
            else:
                node = node.left
    return TreeNode(val)


def print_all_nodes(root):
    queue = deque([root])
    while queue:
        nodes_in_current_level = len(queue)
        # do some logic here for the current level

        for _ in range(nodes_in_current_level):
            node = queue.popleft()

            # do some logic here on the current node
            print(node.val)

            # put the next level onto the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def test1():
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(7)
    node4 = TreeNode(1)
    node5 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    print_all_nodes(insertIntoBST(node1, 5))


test1()
