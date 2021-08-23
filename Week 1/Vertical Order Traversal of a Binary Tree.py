# Definition for a binary tree node.
from collections import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        result = []
        nodes = []
        self.dfs(root,nodes,0,0)
        nodes.sort()
        
        temp = []
        curr = nodes[0][0]
        for i in range(len(nodes)):
            if nodes[i][0] == curr:
                temp.append(nodes[i][2])
            else:
                result.append(temp)
                temp = [nodes[i][2]]
                curr = nodes[i][0]
        result.append(temp)
        return result
    
    def dfs(self,node,nodes,row,col):
        nodes.append((col,row,node.val))
        if node.left:
            self.dfs(node.left,nodes,row + 1,col - 1)
        if node.right:
            self.dfs(node.right,nodes,row + 1, col + 1)
        
                
            