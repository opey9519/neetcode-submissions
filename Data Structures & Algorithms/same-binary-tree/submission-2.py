# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Visit each node, if exist and vals match, return True; else False
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Case 1: Both nodes don't exist
        if not p and not q:
            return True
        # Case 2: Both nodes exist AND their values match -> check more nodes
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # Case 3: Return False if these conditions are not met
        else:
            return False