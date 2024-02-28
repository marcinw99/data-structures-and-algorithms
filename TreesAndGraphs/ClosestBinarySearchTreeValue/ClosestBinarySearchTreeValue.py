from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closestValue(root: Optional[TreeNode], target: float) -> int:
    current_value_diff = abs(target - root.val)

    if target < root.val and root.left is not None:
        left = closestValue(root.left, target)
        left_diff = abs(target - left)
        if left_diff < current_value_diff:
            return left
        elif left_diff > current_value_diff:
            return root.val
        else:
            return min(left, root.val)
    elif target > root.val and root.right is not None:
        right = closestValue(root.right, target)
        right_diff = abs(target - right)
        if right_diff < current_value_diff:
            return right
        elif right_diff > current_value_diff:
            return root.val
        else:
            return min(right, root.val)

    return root.val


# TODO https://leetcode.com/problems/closest-binary-search-tree-value/editorial/


def test1():
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(5)
    node4 = TreeNode(1)
    node5 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    print(closestValue(node1, 3.714286))  # 4


def test2():
    node1 = TreeNode(1)
    print(closestValue(node1, 4.428571))  # 1


test1()
test2()
