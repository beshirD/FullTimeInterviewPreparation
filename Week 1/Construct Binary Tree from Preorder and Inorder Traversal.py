# Definition for a binary tree node.
from collections import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index = [0]
        inorder_dict = {}
        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i
        return self.construct_BT(preorder,inorder_dict,0,len(inorder) - 1, index)
            
    def construct_BT(self,preorder,inorder_dict,start, end,index):
        if start > end:
            return None
        root = TreeNode(preorder[index[0]])
        idx = inorder_dict[preorder[index[0]]]
        index[0] += 1
        root.left = self.construct_BT(preorder,inorder_dict,start,idx - 1,index)
        root.right = self.construct_BT(preorder,inorder_dict,idx + 1,end,index)
        
        return root