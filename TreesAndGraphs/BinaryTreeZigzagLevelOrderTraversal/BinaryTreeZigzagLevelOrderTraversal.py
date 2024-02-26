from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_zigzag_level_order_traversal_additional_loop(root: TreeNode) -> List[List[int]]:
    answer = []
    last_iterated_from_left = False

    queue = deque([root])

    while len(queue) > 0:
        current_level_length = len(queue)
        current_level_values = []

        iteration_range = range(current_level_length - 1, -1, -1) if last_iterated_from_left else range(
            current_level_length)
        for i in iteration_range:
            current_level_values.append(queue[i].val)
        last_iterated_from_left = not last_iterated_from_left

        answer.append(current_level_values)

        for _ in range(current_level_length):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return answer


def binary_tree_zigzag_level_order_traversal_additional_loop_better(root: TreeNode) -> List[List[int]]:
    answer = []
    last_iterated_from_left = False

    queue = deque([root])

    while len(queue) > 0:
        current_level_length = len(queue)
        current_level_values = []

        if last_iterated_from_left:
            for i in range(current_level_length - 1, -1, -1):
                current_level_values.append(queue[i].val)

        for _ in range(current_level_length):
            node = queue.popleft()
            if not last_iterated_from_left:
                current_level_values.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        answer.append(current_level_values)
        last_iterated_from_left = not last_iterated_from_left

    return answer


def binary_tree_zigzag_level_order_traversal_simpler_bfs(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    answer = []
    should_insert_reversed = False

    queue = deque([root])

    while len(queue) > 0:
        current_level_length = len(queue)
        level_values = deque()

        for _ in range(current_level_length):
            node = queue.popleft()

            if should_insert_reversed:
                level_values.appendleft(node.val)
            else:
                level_values.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        answer.append(list(level_values))
        should_insert_reversed = not should_insert_reversed

    return answer


# from LC
def binary_tree_zigzag_level_order_traversal_dfs(root: TreeNode) -> List[List[int]]:
    if root is None:
        return []

    results = []

    def dfs(node, level):
        if level >= len(results):
            results.append(deque([node.val]))
        else:
            if level % 2 == 0:
                results[level].append(node.val)
            else:
                results[level].appendleft(node.val)

        for next_node in [node.left, node.right]:
            if next_node is not None:
                dfs(next_node, level + 1)

    # normal level order traversal with DFS
    dfs(root, 0)

    return results


def test1():
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node1.left = node2
    node1.right = node3
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node3.left = node4
    node3.right = node5
    print(binary_tree_zigzag_level_order_traversal_simpler_bfs(node1))


test1()
