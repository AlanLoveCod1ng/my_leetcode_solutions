# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue1 = deque([root])
        queue2 = deque([])
        result = []
        level_num = 0
        while len(queue1) != 0:
            current_level_vals = []
            while len(queue1) != 0:
                current_node = queue1.popleft()
                current_level_vals.append(current_node.val)
                if current_node.left:
                    queue2.append(current_node.left)
                if current_node.right:
                    queue2.append(current_node.right)
            if level_num % 2 == 1:
                current_level_vals.reverse()
            result.append(current_level_vals)
            queue1 = queue2
            queue2 = deque([])
            level_num += 1
        return result