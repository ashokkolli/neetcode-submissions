# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Similar to the 
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # helper returns (height, is_balanced) for the subtree at 'node'
        def dfs(node):
            # empty subtree: height 0, and it IS balanced
            if not node:
                return (0, True)

            # dive into both sides first (post-order DFS)
            left_height, left_balanced = dfs(node.left)
            right_height, right_balanced = dfs(node.right)

            # this node's height = tallest side + 1 for itself
            height = 1 + max(left_height, right_height)

            # this node is balanced only if BOTH sides are balanced
            # AND its own two heights differ by at most 1
            balanced = (left_balanced and right_balanced
                        and abs(left_height - right_height) <= 1)

            return (height, balanced)

        # we only care about the balanced flag (index 1)
        return dfs(root)[1]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().isBalanced(root))   # expected: True

'''
Time is O(n) — each node visited once, height and balance computed together in one pass. Space is O(h) for the recursion stack, O(log n) balanced down to O(n) for a skewed tree."
'''

'''
Running Speech (say this while coding)

"A tree is balanced if, for every node, the heights of its left and right subtrees differ by at most one. The important word is every — one bad node anywhere makes the whole tree unbalanced, so I can't just check the root.
The naive way would be: for each node, call a height function on its left and right, compare them. But that recomputes heights over and over — it's O(n²). I can do better.
The trick is the same pattern as Diameter: a single post-order DFS that returns two things at once — the height of the subtree, and whether that subtree is balanced. By computing height on the way up, I never recompute it.
So my helper returns a tuple, height and a balanced flag. Base case is an empty node: height zero, and it's balanced by definition. For a real node, I recurse left and right first — that's the post-order part, I need the children's results before I can decide anything. Then the height is one plus the taller side.
The current node is balanced only if three things hold: the left subtree is balanced, the right subtree is balanced, and the two heights differ by at most one. If any node deep down failed, that False propagates up through the AND, so the root's answer reflects the whole tree.
At the top I just return the balanced flag. Let me trace it quickly... [walk the example]. That gives True, correct.
Time is O(n) — each node visited once, height and balance computed together in one pass. Space is O(h) for the recursion stack, O(log n) balanced down to O(n) for a skewed tree."

'''