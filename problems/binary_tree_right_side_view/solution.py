# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue1 = deque([root])
        queue2 = deque([])
        result = []
        while queue1:
            first = True
            while queue1:
                current = queue1.popleft()
                if first:
                    result.append(current.val)
                    first = False
                if current.right:
                    queue2.append(current.right)
                if current.left:
                    queue2.append(current.left)
            queue1 = queue2
            queue2 = deque([])
        return result
                