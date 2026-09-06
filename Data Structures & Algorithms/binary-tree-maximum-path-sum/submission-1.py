# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Global variable
        res = [root.val]

        # Return maximum path sum without splitting
        def dfs(root):
            # Base Case: if no root -> Return 0 b/c adding
            if not root:
                return 0

            # Explore subtrees
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # Update to 0 to not include val IF negative
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Update max including root
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return maximum subtree + root to parent
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]

