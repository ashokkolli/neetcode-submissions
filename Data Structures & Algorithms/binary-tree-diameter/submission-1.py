# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#⭐️⭐️⭐️ 🚀 read this first 100% https://docs.google.com/document/d/1xwHHAL23bj89ROwpeOzy29hGoJYVAXcQ8ElsYgDnmFU/edit?tab=t.0
# LeetCode pre-defines TreeNode; in a blank editor, define it yourself
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        # helper returns (height, diameter) for the subtree at 'node'
        def dfs(node):
            # empty subtree: height 0, diameter 0
            if not node:
                return (0, 0)

            # dive into both sides first (post-order DFS)
            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)

            # this node's height = tallest side + 1 for itself
            height = 1 + max(left_height, right_height)

            # best diameter: left's best, right's best, or path through HERE
            diameter = max(left_diameter, right_diameter,
                           left_height + right_height)

            return (height, diameter)

        # take the diameter (index 1); height was only internal
        return dfs(root)[1]


# build a small tree and call it (interview test harness)
#         1
#        / \
#       2   3
#      / \
#     4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().diameterOfBinaryTree(root))   # expected: 3
