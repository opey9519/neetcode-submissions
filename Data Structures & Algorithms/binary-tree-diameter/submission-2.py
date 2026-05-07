# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftHeight = self.findHeight(root.left)
        rightHeight = self.findHeight(root.right)
        diameter = leftHeight + rightHeight
        sub = max(self.diameterOfBinaryTree(root.left),
                  self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)

        
    
    def findHeight(self, root):
        if not root:
            return 0
        
        return 1 + max(self.findHeight(root.left), self.findHeight(root.right))