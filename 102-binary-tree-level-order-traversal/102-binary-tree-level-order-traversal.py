# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue1 = deque([root])
        queue2 = deque([])
        result = []
        while len(queue1) != 0:
            current_level_vals = []
            while len(queue1) != 0:
                current_node = queue1.popleft()
                current_level_vals.append(current_node.val)
                if current_node.left:
                    queue2.append(current_node.left)
                if current_node.right:
                    queue2.append(current_node.right)
            result.append(current_level_vals)
            queue1 = queue2
            queue2 = deque([])
        return result
            
        
        