# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Scan distance between all nodes by summing left & right subtrees
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root:
            return 0
        
        # Gather subtree heights
        leftHeight = self.getMaxHeight(root.left)
        rightHeight = self.getMaxHeight(root.right)
        # Potential Diameter
        subTreeSum = leftHeight + rightHeight
        diameter = max(self.diameterOfBinaryTree(root.left),
                       self.diameterOfBinaryTree(root.right))
        # Compare current SubTree versus Diameter starting from other roots
        return max(diameter, subTreeSum)

    
    # Helper function get max height of tree starting from root
    def getMaxHeight(self, root):
        if not root:
            return 0
        
        return 1 + max(self.getMaxHeight(root.left), self.getMaxHeight(root.right))