# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.inorder(root,arr)
        
        l = len(arr)
        return self.constructBST(arr, 0, l)
    
    def constructBST(self, arr, s, e):
        if s >= e:
        
            return None
        
        rootIndex = (e + s)//2
        
        node = TreeNode(arr[rootIndex])
        node.left = self.constructBST(arr, s, rootIndex)
        node.right = self.constructBST(arr, rootIndex + 1, e)
        return node

    def inorder(self,node,arr):
        if node.left:
            self.inorder(node.left,arr)
        arr.append(node.val)
        if node.right:
            self.inorder(node.right,arr)