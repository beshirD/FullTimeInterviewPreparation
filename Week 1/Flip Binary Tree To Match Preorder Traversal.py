# Definition for a binary tree node.
from collections import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        index = [0]
        possible = [True]
        swap = []
        self.dfs(root,voyage,index,swap,possible)
        return (swap, [-1])[possible[0]]
    
    def dfs(self,node,voyage,index,swap,possible):
        if node:    
            if node.val != voyage[index[0]]:
                possible[0] = False
                return
            if node.left and node.left.val != voyage[index[0] + 1]:
                node.left, node.right = node.right, node.left
                swap.append(node.val)
            index[0] += 1
            self.dfs(node.left,voyage,index,swap,possible)
            self.dfs(node.right,voyage,index,swap,possible)
        