# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            self.dfs(root)

    def dfs(self,node):
        if not node.left and not node.right:
            return node
        
        left_last , right_last = None, None        
        if node.left:
            left_last = self.dfs(node.left)
        if node.right:
            right_last = self.dfs(node.right)
    
        right = node.right
        
        if node.left:
            node.right = node.left
            node.left = None
            
        if left_last:
            left_last.right = right
        
        return right_last if right_last else left_last