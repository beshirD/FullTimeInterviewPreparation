from collections import defaultdict
class Solution:
    def solve(self, left, right):
        left_set = set(left)
        right_set = set(right)
        visited = set()
        root = -2
        
        #choose start point
        for i in range(len(left)):
            if i not in left_set and i not in right_set:
                root = i
                break
    
        #return False if no start point
        if root == -2:
            return False

        valid = self.dfs(root,left,right,visited)

        return (len(visited) == len(left)) and valid
    def dfs(self,node,left,right,visited): 
        visited.add(node)

        for child in [left[node],right[node]]:
            if child != -1:
                if child in visited:
                    return False
                    
                if not self.dfs(child,left,right,visited):
                    return False
                
        return True

        
        
        
        
        
