# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        robbed_dict = {}
        not_robbed_dict = {}
       
        return self.rob_house(root,robbed_dict,not_robbed_dict,False)
    
    def rob_house(self,node,robbed_dict,not_robbed_dict,parent_robbed):
        if not node:
            return 0
        
        if parent_robbed:
            if node in not_robbed_dict:
                return not_robbed_dict[node]
            
            not_robbed_dict[node] = self.rob_house(node.left,robbed_dict,not_robbed_dict,False) +                                                       self.rob_house(node.right,robbed_dict,not_robbed_dict,False)
            
            return not_robbed_dict[node]
        else:
            
            if node in robbed_dict:
                return robbed_dict[node]
            
            rob = node.val + self.rob_house(node.left,robbed_dict,not_robbed_dict,True) +                                             self.rob_house(node.right,robbed_dict,not_robbed_dict,True)
            
            not_rob = self.rob_house(node.left,robbed_dict,not_robbed_dict,False) +                                                       self.rob_house(node.right,robbed_dict,not_robbed_dict,False)
            
            robbed_dict[node] = max(rob,not_rob)
            
            return robbed_dict[node]