# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base Case: There is nothing to traverse 
        if not root or not p or not q:
            return None
        # If cur value is greater than max of p and q, must go lesser nodes
        elif (root.val > max(p.val, q.val)):
            return self.lowestCommonAncestor(root.left, p, q)
        # if cur value is less than min of p and q, must go greater nodes
        elif (root.val < min(p.val, q.val)):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root