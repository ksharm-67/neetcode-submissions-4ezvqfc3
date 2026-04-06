# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def height(r):
            if r is None:
                return 0;

            left = height(r.left)
            right = height(r.right)
    
            d = left + right
            self.maxD = max(self.maxD, d)

            return 1 + max(left, right)

        self.maxD = 0
        height(root)
        return self.maxD


