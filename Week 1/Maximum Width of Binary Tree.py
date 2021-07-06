
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        answer = 0
        queue = deque([(root,0)])
        while queue:
            size = len(queue)
            min_index = float("inf")
            max_index = 0
            for i in range(size):
                current  = queue.popleft()
                min_index = min(min_index,current[1])
                max_index = max(max_index,current[1])
                if current[0].left:
                    queue.append((current[0].left,current[1]*2))
                    
                if current[0].right:
                    queue.append((current[0].right,current[1]*2 + 1))
            answer = max(answer, max_index - min_index + 1)
        return answer
                    
                
        
        