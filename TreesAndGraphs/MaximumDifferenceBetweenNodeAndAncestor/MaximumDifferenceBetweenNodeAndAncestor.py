class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_ancestor_diff(root: TreeNode) -> int:
    def dfs(node: TreeNode, min_encountered: int, max_encountered: int) -> int:
        if node is None:
            return max_encountered - min_encountered

        new_min_encountered = min(min_encountered, node.val)
        new_max_encountered = max(max_encountered, node.val)

        left = dfs(node.left, new_min_encountered, new_max_encountered)
        right = dfs(node.right, new_min_encountered, new_max_encountered)

        return max(left, right)

    return dfs(root, root.val, root.val)


node1 = TreeNode(8)
node2 = TreeNode(3)
node3 = TreeNode(10)
node4 = TreeNode(1)
node5 = TreeNode(6)
node6 = TreeNode(14)
node7 = TreeNode(4)
node8 = TreeNode(7)
node9 = TreeNode(13)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node5.left = node7
node5.right = node8
node6.right = node9

print(max_ancestor_diff(node1))
